# Regular packages
import os

import pandas as pd

# Specific imports from reportlab
from reportlab.platypus import (
    BaseDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageTemplate,
    Frame,
    CondPageBreak,
)
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# This import facilitates the header creation
from functools import partial

# SVG file function
from svglib.svglib import svg2rlg

# These are custom functions
# from facility_report_plots import user_plot, publication_plot
from input_data import Facility_data, Funding
from colour_science_2020 import SCILIFE_COLOURS_GREYS, SCILIFE_COLOURS


def header(canvas, doc, content):
    """
    header creates a header for a reportlabs document, and is inserted in the template
    """
    canvas.saveState()
    w, h = content.wrap(doc.width, doc.topMargin)
    content.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)
    p = canvas.beginPath()
    p.moveTo(doc.leftMargin, doc.height + doc.topMargin - h - 2 * mm)
    p.lineTo(doc.leftMargin + w, doc.height + doc.topMargin - h - 2 * mm)
    p.close()
    canvas.setLineWidth(0.5)
    canvas.setStrokeColor(SCILIFE_COLOURS_GREYS[1])
    canvas.drawPath(p, stroke=1)
    canvas.restoreState()


def generatePdf(facility_name, Facility_data, Funding, current_year):
    """
    generatePdf creates a PDF document based on the reporting data supplied.
    It is using very strict formatting, but is quite simple to edit.
    This function will print the name of the facility its working on, and
    any warnings that may arise. The excel document can be edited to fix warnings
    and to change the information in the PDFs.
    """
    print("\nFacility report {}: {}".format(current_year, facility_name))
    if not os.path.isdir("pdfs_onepagers/"):
        os.mkdir("pdfs_onepagers/")
    # Setting the document sizes and margins. showBoundary is useful for debugging
    doc = BaseDocTemplate(
        "pdfs_onepagers/{}_{}.pdf".format(
            current_year, facility_name.lower().replace(" ", "_")
        ),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=14 * mm,
        topMargin=16 * mm,
        bottomMargin=20 * mm,
        showBoundary=0,
    )
    # These are the fonts available, in addition to a number of "standard" fonts.
    # These are used in setting paragraph styles
    pdfmetrics.registerFont(TTFont("Lato-B", "Lato-Black.ttf"))  # looks bolder
    pdfmetrics.registerFont(TTFont("Lato", "Lato-Regular.ttf"))
    # I have used spaceAfter, spaceBefore and leading to change the layout of the "paragraphs" created with these styles
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="onepager_inner_heading",
            parent=styles["Heading1"],
            fontName="Lato-B",
            fontSize=10,
            color="#FF00AA",
            leading=16,
            spaceAfter=0,
            spaceBefore=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="onepager_chart_heading",
            parent=styles["Heading1"],
            fontName="Lato-B",
            fontSize=10,
            color="#FF00AA",
            leading=16,
            spaceAfter=4,
            spaceBefore=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="onepager_title",
            parent=styles["Heading1"],
            fontName="Lato-B",
            fontSize=16,
            bold=0,
            color="#000000",
            leading=16,
            spaceBefore=0,
        )
    )
    styles.add(
        ParagraphStyle(
            name="onepager_text",
            parent=styles["Normal"],
            fontName="Lato",
            fontSize=10,
            bold=0,
            color="#000000",
            leading=14,
        )
    )
    styles.add(
        ParagraphStyle(
            name="onepager_footnote",
            parent=styles["Normal"],
            fontName="Lato",
            fontSize=7,
            bold=0,
            color="#000000",
            leading=14,
            spaceBefore=20,
        )
    )
    # The document is set up with two frames, one frame is one column, and their widths are set according to SciLifeLab design policy
    frame1 = Frame(
        doc.leftMargin,
        doc.bottomMargin + (doc.height / 2),
        doc.width / 3,  # - 3.5 * mm,
        (doc.height / 2) - 18 * mm,
        id="col1",
        #        showBoundary=1,
        leftPadding=0 * mm,
        topPadding=5 * mm,
        rightPadding=0 * mm,
        bottomPadding=0 * mm,
    )
    frame2 = Frame(
        doc.leftMargin + doc.width / 3 + 2 * mm,  # 2 + 3.5 * mm,
        doc.bottomMargin + (doc.height / 2),
        doc.width / 3,  # 2 - 3.5 * mm,
        (doc.height / 2) - 18 * mm,
        id="col2",
        #        showBoundary=1,
        leftPadding=0 * mm,
        topPadding=5 * mm,
        rightPadding=0 * mm,
        bottomPadding=0 * mm,
    )
    frame3 = Frame(
        doc.leftMargin + (3.5 * mm) + doc.width * 0.61,
        doc.bottomMargin + (doc.height / 2),
        doc.width / 2.7,  # 2 - 3.5 * mm,
        (doc.height / 2) - 18 * mm,
        id="col3",
        #        showBoundary=1,
        leftPadding=0 * mm,
        topPadding=5 * mm,
        rightPadding=0 * mm,
        bottomPadding=0 * mm,
    )
    # top 3 frames contain the text
    # Next frames the Figures
    # Bar charts go first - divide the page in halves for them
    frame4 = Frame(
        doc.leftMargin,
        doc.bottomMargin + (doc.height / 4),
        doc.width / 2,  # 2 - 3.5 * mm,
        (doc.height / 4),  # + 50 * mm,  # - 18 * mm,
        id="pic1",
        #        showBoundary=1,
        leftPadding=0 * mm,
        topPadding=3 * mm,
        rightPadding=0 * mm,
        bottomPadding=0 * mm,
    )
    frame5 = Frame(
        doc.leftMargin + (doc.width / 2),
        doc.bottomMargin + (doc.height / 4),
        doc.width / 2,  # 2 - 3.5 * mm,
        (doc.height / 4),  # + 50 * mm,  # - 18 * mm,
        id="pic2",
        #        showBoundary=1,
        leftPadding=0 * mm,
        topPadding=3 * mm,
        rightPadding=0 * mm,
        bottomPadding=0 * mm,
    )
    # NOW 3 PIE CHARTS
    frame6 = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width / 3,  # 2 - 3.5 * mm,
        (doc.height / 4),  # + 50 * mm,  # - 18 * mm,
        id="pic3",
        #        showBoundary=1,
        leftPadding=0 * mm,
        topPadding=0 * mm,
        rightPadding=0 * mm,
        bottomPadding=0 * mm,
    )
    frame7 = Frame(
        doc.leftMargin + doc.width / 3,
        doc.bottomMargin,
        doc.width / 3,  # 2 - 3.5 * mm,
        (doc.height / 4),  # + 50 * mm,  # - 18 * mm,
        id="pic4",
        #        showBoundary=1,
        leftPadding=0 * mm,
        topPadding=0 * mm,
        rightPadding=0 * mm,
        bottomPadding=0 * mm,
    )
    frame8 = Frame(
        doc.leftMargin + doc.width / 3 + doc.width / 3,
        doc.bottomMargin,
        doc.width / 3,  # 2 - 3.5 * mm,
        (doc.height / 4),  # + 50 * mm,  # - 18 * mm,
        id="pic5",
        #        showBoundary=1,
        leftPadding=0 * mm,
        topPadding=0 * mm,
        rightPadding=0 * mm,
        bottomPadding=0 * mm,
    )
    header_content = Paragraph(
        "<b>{}</b><br/><font name=Lato size=12> {} platform</font>".format(
            (Facility_data["Facility"]).to_string(index=False),
            (Facility_data["Platform"]).to_string(index=False),
        ),
        styles["onepager_title"],
    )
    template = PageTemplate(
        id="test",
        frames=[frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8],
        onPage=partial(header, content=header_content),
    )
    doc.addPageTemplates([template])
    # frames=[frame1,frame2]
    # The Story list will contain all Paragraph and other elements. In the end this is used to build the document
    Story = []
    ### Below here will be Paragraph and Image elements added to the Story, they flow through frames automatically,
    ### however I have set a framebreak to correctly organise things in left/right column.
    Story.append(
        Paragraph(
            "<font color='#A7C947' name=Lato-B><b>Basic information</b></font>",
            styles["onepager_inner_heading"],
        )
    )
    # Drug Discovery and Development (DDD) is a platform. needs different formatting
    if facility_name == "Drug Discovery and Development":
        Story.append(
            Paragraph(
                "<font name=Lato-B><b>Platform directors: </b></font> {}".format(
                    (Facility_data["FD"]).to_string(index=False),
                ),
                styles["onepager_text"],
            )
        )
        Story.append(
            Paragraph(
                "<font name=Lato-B><b>SciLifeLab platform since: </b></font> {}".format(
                    (Facility_data["SLL_since"]).to_string(index=False),
                ),
                styles["onepager_text"],
            )
        )
    else:
        Story.append(
            Paragraph(
                "<font name=Lato-B><b>Facility director(s): </b></font> {}".format(
                    (Facility_data["FD"]).to_string(index=False),
                ),
                styles["onepager_text"],
            )
        )
        Story.append(
            Paragraph(
                "<font name=Lato-B><b>Head(s) of facility: </b></font> {}".format(
                    (Facility_data["HOF"]).to_string(index=False),
                ),
                styles["onepager_text"],
            )
        )
        Story.append(
            Paragraph(
                "<font name=Lato-B><b>SciLifeLab facility since: </b></font> {}".format(
                    (Facility_data["SLL_since"]).to_string(index=False),
                ),
                styles["onepager_text"],
            )
        )
    pd.options.display.max_colwidth = 600
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Host university: </b></font>{}".format(
                (Facility_data["H_uni"]).to_string(index=False),
            ),
            styles["onepager_text"],
        )
    )
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>FTEs: </b></font>{}".format(
                (Facility_data["FTEs"]).to_string(index=False),
            ),
            styles["onepager_text"],
        )
    )
    Story.append(
        Paragraph(
            u"<font name=Lato-B><b>FTEs financed by SciLifeLab: </b></font>{}".format(
                (Facility_data["SLL_FTEs"]).to_string(index=False),
            ),
            styles["onepager_text"],
        )
    )
    Story.append(
        Paragraph(
            "<font color='#A7C947'><font name=Lato-B><b>Funding in {} (kSEK)</b></font></font>".format(
                current_year
            ),
            styles["onepager_inner_heading"],
        )
    )
    # Funding (need to have Scilifelab, other sources and then total)
    # SLL funding in file provided by OO. Calculated total using this and 'other funding'
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>SciLifeLab: </b></font>{}".format(
                (Facility_data["Amount (kSEK)"]).to_string(index=False),
            ),
            styles["onepager_text"],
        )
    )
    # Scilifelab funding is in funding data and total funding is in there too, but other financiers vary
    # Need to take out Scilifelab funding and total funding to be able to go through other funders without issue
    fundwosll = Funding[~Funding.Financier.eq("SciLifeLab")]
    fundwoslltot = fundwosll[~fundwosll.Financier.eq("Total")]
    for i in fundwoslltot["Financier"].unique():
        temp = fundwoslltot[(fundwoslltot["Financier"] == i)]
        if temp is not None:
            Story.append(
                Paragraph(
                    "<font name=Lato-B><b>{}: </b></font>{}".format(
                        i,
                        temp["Amount (kSEK)"][
                            temp["Amount (kSEK)"].first_valid_index()
                        ],
                    ),
                    styles["onepager_text"],
                )
            )
    # now a line above the total value
    Story.append(
        HRFlowable(
            width="40%",
            thickness=0.5,
            lineCap="round",
            color=SCILIFE_COLOURS_GREYS[1],
            spaceBefore=1,
            spaceAfter=1,
            hAlign="LEFT",
            vAlign="BOTTOM",
            dash=None,
        )
    )
    # now the totals
    fundstot = Funding[Funding.Financier.eq("Total")]
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Total: </b></font>{}".format(
                (fundstot["Amount (kSEK)"]).to_string(index=False),
            ),
            styles["onepager_text"],
        )
    )
    Story.append(CondPageBreak(100 * mm))
    ### RESOURCE ALLOCATION
    total_percentage = total_percentage = (
        int(Facility_data["RA_nat"])
        + int(Facility_data["RA_int"])
        + int(Facility_data["RA_tech"])
        + int(Facility_data["RA_Ind"])
        + int(Facility_data["RA_Health"])
        + int(Facility_data["RA_ogov"])
    )
    if total_percentage == 100:
        Story.append(
            Paragraph(
                "<font color='#A7C947'><font name=Lato-B><b>Resource allocation {}</b></font></font>".format(
                    current_year
                ),
                styles["onepager_inner_heading"],
            )
        )
    else:
        print(
            "WARNING: PERCENTAGE DOES NOT ADD UP TO 100 IN RESOURCE_ALLOCATION FOR",
            facility_name,
            total_percentage,
        )
        Story.append(
            Paragraph(
                "<font color='#FF0000'><font name=Lato-B><b>Resource allocation {}</b></font></font>".format(
                    current_year
                ),
                styles["onepager_inner_heading"],
            )
        )
    if int(Facility_data.RA_nat) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["RA_nat"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Academia (national): </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.RA_int) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["RA_int"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Academia (international): </b></font>{}".format(
                tmp_input
            ),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.RA_tech) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["RA_tech"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Internal tech. dev.: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.RA_Ind) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["RA_Ind"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Industry: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.RA_Health) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["RA_Health"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Healthcare: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.RA_ogov) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["RA_ogov"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Other gov. agencies: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    #    Story.append(CondPageBreak(50 * mm))
    ### USER FEES - reagents, instruments...
    total_percentage = (
        int(Facility_data["UF_reag"])
        + int(Facility_data["UF_instr"])
        + int(Facility_data["UF_sal"])
        + int(Facility_data["UF_rent"])
        + int(Facility_data["UF_other"])
    )
    if total_percentage == 100:
        Story.append(
            Paragraph(
                "<font color='#A7C947'><font name=Lato-B><b>User Fees {}</b></font></font>".format(
                    current_year
                ),
                styles["onepager_inner_heading"],
            )
        )
    else:
        print(
            "WARNING: PERCENTAGE DOES NOT ADD UP TO 100 IN COSTS FOR",
            facility_name,
            total_percentage,
        )
        Story.append(
            Paragraph(
                "<font color='#FF0000'><font name=Lato-B><b>User Fees {}</b></font></font>".format(
                    current_year
                ),
                styles["onepager_inner_heading"],
            )
        )

    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Total (kSEK): </b></font>{}".format(
                (Facility_data["UF_Tot"]).to_string(index=False),
            ),
            styles["onepager_text"],
        )
    )

    Story.append(
        HRFlowable(
            width="40%",
            thickness=0.5,
            lineCap="round",
            color=SCILIFE_COLOURS_GREYS[1],
            spaceBefore=1,
            spaceAfter=1,
            hAlign="LEFT",
            vAlign="BOTTOM",
            dash=None,
        )
    )
    if int(Facility_data.UF_reag) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["UF_reag"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Reagents: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.UF_instr) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["UF_instr"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Instrument: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.UF_sal) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["UF_sal"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Salaries: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.UF_rent) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["UF_rent"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Rent: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.UF_other) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["UF_other"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Other: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    Story.append(CondPageBreak(100 * mm))
    ### USER FEES BY SECTOR
    total_percentage = (
        int(Facility_data["UF_sect_nat"])
        + int(Facility_data["UF_sect_int"])
        + int(Facility_data["UF_sect_ind"])
        + int(Facility_data["UF_sect_health"])
        + int(Facility_data["UF_sect_othgov"])
    )
    if total_percentage == 100:
        Story.append(
            Paragraph(
                "<font color='#A7C947'><font name=Lato-B><b>User fees by sector {}</b></font></font>".format(
                    current_year
                ),
                styles["onepager_inner_heading"],
            )
        )
    else:
        print(
            "WARNING: PERCENTAGE DOES NOT ADD UP TO 100 IN USER FEES FOR",
            facility_name,
            total_percentage,
        )
        Story.append(
            Paragraph(
                "<font color='#FF0000'><font name=Lato-B><b>User fees by sector {}</b></font></font>".format(
                    current_year
                ),
                styles["onepager_inner_heading"],
            )
        )
    if int(Facility_data.UF_sect_nat) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["UF_sect_nat"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Academia (national): </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.UF_sect_int) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["UF_sect_int"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Academia (international): </b></font>{}".format(
                tmp_input
            ),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.UF_sect_ind) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["UF_sect_ind"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Industry: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.UF_sect_health) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["UF_sect_health"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Healthcare: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    if int(Facility_data.UF_sect_othgov) == 0:
        tmp_input = "-"
    else:
        tmp_input = "{}%".format(int(Facility_data["UF_sect_othgov"]))
    Story.append(
        Paragraph(
            "<font name=Lato-B><b>Other gov. agencies: </b></font>{}".format(tmp_input),
            styles["onepager_text"],
        )
    )
    # Story.append(CondPageBreak(50 * mm))
    #### SERVICES
    Story.append(
        Paragraph(
            "<font color='#A7C947'><font name=Lato-B><b>Services</b></font></font>",
            styles["onepager_inner_heading"],
        )
    )

    if Facility_data["Services"].notnull:
        pd.options.display.max_colwidth = 600
        bullet_pointing = Facility_data["Services"].to_string(index=False)
        bullet_points = bullet_pointing.replace("\\n", "*")
        bullet_points = bullet_points.split("*")  # .explode(bullet_points)
        for bullet in bullet_points:
            Story.append(Paragraph(bullet, styles["onepager_text"]))
    else:
        Story.append(
            Paragraph(
                "Service information goes here, please input text in excel file",
                styles["onepager_text"],
            )
        )
    # special notes
    # This puts an asterisk at the bottom of the services, with some info if there was any in the data file
    if facility_name == "Mass Cytometry (KI)":
        Story.append(
            Paragraph(
                "Note: publication data is combined for the two Mass Cytometry facilities",
                styles["onepager_footnote"],
            )
        )
    elif facility_name == "Mass Cytometry (LiU)":
        Story.append(
            Paragraph(
                "Note: publication data is combined for the two Mass Cytometry facilities",
                styles["onepager_footnote"],
            )
        )
    else:
        print("no special notes for this facility")

    # Now I need to put in the Figures.. (5 plots if data is available for everything, or some might be missing)
    # figs already made in .svg format, they need to be imported
    Story.append(CondPageBreak(200 * mm))  # move to next frame
    # pubs by cat first, then pubs by JIF
    Story.append(
        Paragraph(
            "<font color='#A7C947' name=Lato-B><b>Publication by category</b></font>",
            styles["onepager_chart_heading"],
        )
    )
    filepath_cats = "/Users/liahu895/Documents/GitHub/IAB_2021/Facility_one_pagers/Updated_2021scripts/Plots/pubcat_plots/{}_cats.svg".format(
        (facility_name),
    )
    isFile_cats = os.path.isfile(filepath_cats)
    if isFile_cats == True:
        im_cats = svg2rlg(filepath_cats)
        im_cats = Image(im_cats, width=70 * mm, height=55 * mm)
        im_cats.hAlign = "CENTER"
        Story.append(im_cats)
    else:
        Story.append(
            Paragraph(
                "No publication data available",
                styles["onepager_text"],
            )
        )
    # Now JIF barchart
    Story.append(CondPageBreak(200 * mm))  # move to next frame
    Story.append(
        Paragraph(
            "<font color='#A7C947' name=Lato-B><b>Publication by Journal Impact Factor</b></font>",
            styles["onepager_chart_heading"],
        )
    )
    filepath_JIF = "/Users/liahu895/Documents/GitHub/IAB_2021/Facility_one_pagers/Updated_2021scripts/Plots/JIF_plots/{}_JIF.svg".format(
        (facility_name),
    )
    isFile_JIF = os.path.isfile(filepath_JIF)
    if isFile_JIF == True:
        im_JIF = svg2rlg(filepath_JIF)
        im_JIF = Image(im_JIF, width=70 * mm, height=55 * mm)
        im_JIF.hAlign = "CENTER"
        Story.append(im_JIF)
    else:
        Story.append(
            Paragraph(
                "No publication data available",
                styles["onepager_text"],
            )
        )
    Story.append(CondPageBreak(200 * mm))  # move to next frame
    #
    # Now the pie charts (in the lowest part of the page)- ascending year left to right
    Story.append(
        Paragraph(
            "<font color='#A7C947' name=Lato-B><b>Users {}</b></font>".format(
                int(current_year) - 2
            ),
            styles["onepager_chart_heading"],
        )
    )
    filepath_u18 = "/Users/liahu895/Documents/GitHub/IAB_2021/Facility_one_pagers/Updated_2021scripts/Plots/Aff_Pies/{}_{}_affs.svg".format(
        (facility_name),
        (int(current_year) - 2),
    )
    isFile_u18 = os.path.isfile(filepath_u18)
    if isFile_u18 == True:
        im_u18 = svg2rlg(filepath_u18)
        im_u18 = Image(im_u18, width=58 * mm, height=58 * mm)
        im_u18.hAlign = "CENTER"
        Story.append(im_u18)
    else:
        Story.append(
            Paragraph(
                "No user information",
                styles["onepager_text"],
            )
        )
    Story.append(CondPageBreak(200 * mm))  # move to next frame
    Story.append(
        Paragraph(
            "<font color='#A7C947' name=Lato-B><b>Users {}</b></font>".format(
                int(current_year) - 1
            ),
            styles["onepager_chart_heading"],
        )
    )
    filepath_u19 = "/Users/liahu895/Documents/GitHub/IAB_2021/Facility_one_pagers/Updated_2021scripts/Plots/Aff_Pies/{}_{}_affs.svg".format(
        (facility_name),
        (int(current_year) - 1),
    )
    isFile_u19 = os.path.isfile(filepath_u19)
    if isFile_u19 == True:
        im_u19 = svg2rlg(filepath_u19)
        im_u19 = Image(im_u19, width=58 * mm, height=58 * mm)
        im_u19.hAlign = "CENTER"
        Story.append(im_u19)
    else:
        Story.append(
            Paragraph(
                "No user information",
                styles["onepager_text"],
            )
        )
    Story.append(CondPageBreak(200 * mm))  # move to next frame
    Story.append(
        Paragraph(
            "<font color='#A7C947' name=Lato-B><b>Users {}</b></font>".format(
                int(current_year)
            ),
            styles["onepager_chart_heading"],
        )
    )
    filepath_u20 = "/Users/liahu895/Documents/GitHub/IAB_2021/Facility_one_pagers/Updated_2021scripts/Plots/Aff_Pies/{}_{}_affs.svg".format(
        (facility_name),
        (int(current_year)),
    )
    isFile_u20 = os.path.isfile(filepath_u20)
    if isFile_u20 == True:
        im_u20 = svg2rlg(filepath_u20)
        im_u20 = Image(im_u20, width=58 * mm, height=58 * mm)
        im_u20.hAlign = "CENTER"
        Story.append(im_u20)
    else:
        Story.append(
            Paragraph(
                "No user information",
                styles["onepager_text"],
            )
        )

    # Finally, build the document.
    doc.build(Story)


# made a function that will generate all files together
# What works will change every report.
# recommend running the below and then individually checking each one and tweaking
# then comment below out and run for individual facilities (further down)
# Note: 2021 - WABI has no user fees. comment out warning code for this facility

whonow = "National Genomics Infrastructure"
current_year = 2020
test_facs = Facility_data[(Facility_data["Facility"] == whonow)]
test_fund = Funding[(Funding["Facility"] == whonow)]
facility_name = whonow
generatePdf(facility_name, test_facs, test_fund, current_year)
