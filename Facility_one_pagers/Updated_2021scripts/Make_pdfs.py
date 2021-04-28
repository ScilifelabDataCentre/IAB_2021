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
# from svglib.svglib import svg2rlg

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
        )
    )
    # The document is set up with two frames, one frame is one column, and their widths are set according to SciLifeLab design policy
    frame1 = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width / 2 - 3.5 * mm,
        doc.height - 18 * mm,
        id="col1",
        leftPadding=0 * mm,
        topPadding=5 * mm,
        rightPadding=0 * mm,
        bottomPadding=0 * mm,
    )
    # frame2 = Frame(doc.leftMargin+doc.width/2+3.5*mm, doc.bottomMargin, doc.width/2-3.5*mm, doc.height-18*mm, id='col2', leftPadding=0*mm, topPadding=0*mm, rightPadding=0*mm, bottomPadding=0*mm)
    header_content = Paragraph(
        "<b>{}</b><br/><font name=Lato size=12> {} platform</font>".format(
            (Facility_data["Facility"]).to_string(index=False),
            (Facility_data["Platform"]).to_string(index=False),
        ),
        styles["onepager_title"],
    )
    template = PageTemplate(
        id="test", frames=frame1, onPage=partial(header, content=header_content)
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

    Story.append(
        Paragraph(
            "<font color='#A7C947'><font name=Lato-B><b>Services</b></font></font>",
            styles["onepager_inner_heading"],
        )
    )

    if Facility_data["Services"].notnull:
        bullet_points = Facility_data["Services"]
        for bullet in bullet_points:
            Story.append(Paragraph(bullet, styles["onepager_text"]))
    else:
        Story.append(
            Paragraph(
                "Service information goes here, please input text in excel file",
                styles["onepager_text"],
            )
        )

    # This puts an asterisk at the bottom of the page, with some info if there was any in the data file
    if facility_name == "Mass Cytometry (KI)":
        Story.append(
            Paragraph(
                "* Publication data is combined for the two Mass Cytometry facilities",
                styles["onepager_footnote"],
            )
        )
    elif facility_name == "Mass Cytometry (LiU)":
        Story.append(
            Paragraph(
                "* Publication data is combined for the two Mass Cytometry facilities",
                styles["onepager_footnote"],
            )
        )
    else:
        print("no special notes for this facility")

    # Finally, build the document.
    doc.build(Story)


current_year = 2020
test_facs = Facility_data[
    (Facility_data["Facility"] == "Drug Discovery and Development")
]
test_fund = Funding[(Funding["Facility"] == "Drug Discovery and Development")]
facility_name = "Drug Discovery and Development"

generatePdf(facility_name, test_facs, test_fund, current_year)

# for facility in complete_reporting_data.keys():
# 	# Run PDF generation for each facility
# 	generatePdf(facility, complete_reporting_data[facility], current_year)
