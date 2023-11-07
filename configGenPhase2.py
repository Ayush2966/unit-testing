import json

# From 2 to 130
set_number = 75


# Set true if heading and subheading are horizontally arranged
isHorizontal = False

templateSizes = {
    1: {
        "name": "instagram_story",
        "container": {"position": "relative", "height": "1920px", "width": "1080px"},
        "logoContainer": {
            "position": "absolute",
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
            "width": "273px",
            "height": "103px",
        },
        "heading": {
            "fontSize": "67px",
            "lineHeight": "70px",
            "textAlign": "center",
            "fontWeight": "600",
            "color": "#000000",
            "maxWidth": "100%",
        },
        "subHeading": {
            "fontSize": "28px",
            "lineHeight": "38px",
            "textAlign": "center",
            "fontWeight": "400",
            "color": "#484848",
            "maxWidth": "100%",
        },
    },
    2: {
        "name": "x_header",
        "container": {"position": "relative", "height": "500px", "width": "1500px"},
        "logoContainer": {
            "position": "absolute",
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
            "width": "130px",
            "height": "50px",
        },
        "heading": {
            "fontSize": "48px",
            "lineHeight": "52px",
            "textAlign": "center",
            "fontWeight": "600",
            "color": "#000000",
            "maxWidth": "100%",
        },
        "subHeading": {
            "fontSize": "24px",
            "lineHeight": "30px",
            "textAlign": "center",
            "fontWeight": "400",
            "color": "#484848",
            "maxWidth": "100%",
        },
    },
    3: {
        "name": "large_mobile_banner",
        "container": {"position": "relative", "height": "100px", "width": "320px"},
        "logoContainer": {
            "position": "absolute",
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
            "width": "21px",
            "height": "10px",
        },
        "heading": {
            "fontSize": "10px",
            "lineHeight": "12px",
            "textAlign": "center",
            "fontWeight": "600",
            "color": "#000000",
            "maxWidth": "100%",
        },
        "subHeading": {
            "fontSize": "5px",
            "lineHeight": "10px",
            "textAlign": "center",
            "fontWeight": "400",
            "color": "#484848",
            "maxWidth": "100%",
        },
    },
    4: {
        "name": "linkedin_cover",
        "container": {"position": "relative", "height": "396px", "width": "1584px"},
        "logoContainer": {
            "position": "absolute",
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
            "width": "104px",
            "height": "40px",
        },
        "heading": {
            "fontSize": "42px",
            "lineHeight": "48px",
            "textAlign": "center",
            "fontWeight": "600",
            "color": "#000000",
            "maxWidth": "100%",
        },
        "subHeading": {
            "fontSize": "24px",
            "lineHeight": "36px",
            "textAlign": "center",
            "fontWeight": "400",
            "color": "#484848",
            "maxWidth": "100%",
        },
    },
}


template = {
    "container": {},
    "logoContainer": {},
    "logo": {"width": "100%", "height": "100%", "objectFit": "contain"},
    "textContainer": {
        "position": "absolute",
        "display": "flex",
        "flexDirection": "column",
        "justifyContent": "center",
        "width": "100%",
        "top": "0",
        "paddingLeft": "0",
        "paddingRight": "0",
        "gap": "10px",
    },
    "headingContainer": {"width": "100%"},
    "heading": {},
    "subHeadingContainer": {"width": "100%"},
    "subHeading": {},
}

config = {
    "name": "",
    "design": "",
    "layout": "",
    "properties": {**template},
}


def add_px_if_integer(value):
    try:
        int_value = int(value)
        return f"{int_value}px"
    except ValueError:
        return value


if __name__ == "__main__":
    setNumber = set_number
    templateType = int(input("Enter template number: "))
    config["name"] = f"set{setNumber}_{templateSizes[templateType]['name']}"
    config["design"] = f"D{setNumber}"
    config["layout"] = f"{templateSizes[templateType]['name']}".upper()
    fileName = f"set{setNumber}_{templateSizes[templateType]['name']}.json"

    # Update template properties with common values
    template["container"].update(templateSizes[templateType]["container"])
    template["logoContainer"].update(templateSizes[templateType]["logoContainer"])
    template["heading"].update(templateSizes[templateType]["heading"])
    template["subHeading"].update(templateSizes[templateType]["subHeading"])

    # Logo Container Styles

    logo_position = input(
        "Enter logo position (top_left, top_right, bottom_left, bottom_right): "
    )
    logo_position_values = input("Enter logo position values : ")
    logo_position_values = logo_position_values.split(" ")
    if logo_position == "top_left":
        template["logoContainer"]["top"] = f"{logo_position_values[0]}px"
        template["logoContainer"]["left"] = f"{logo_position_values[1]}px"
    elif logo_position == "top_right":
        template["logoContainer"]["top"] = f"{logo_position_values[0]}px"
        template["logoContainer"]["right"] = f"{logo_position_values[1]}px"
    elif logo_position == "bottom_left":
        template["logoContainer"]["bottom"] = f"{logo_position_values[0]}px"
        template["logoContainer"]["left"] = f"{logo_position_values[1]}px"
    elif logo_position == "bottom_right":
        template["logoContainer"]["bottom"] = f"{logo_position_values[0]}px"
        template["logoContainer"]["right"] = f"{logo_position_values[1]}px"

    # Text Container Styles
    textContainerStylesInput = input(
        "Enter text container styles (top, paddingLeft, paddingRight, gap): "
    )
    textContainerStylesValues = textContainerStylesInput.split(" ")
    styles = [
        "top",
        "paddingLeft",
        "paddingRight",
        "gap",
    ]
    template["textContainer"].update(
        {style: f"{value}px" for style, value in zip(styles, textContainerStylesValues)}
    )

    headingAlignment = input("Enter heading alignment: ")
    template["heading"]["textAlign"] = headingAlignment

    subHeadingAlignment = input("Enter subHeading alignment: ")
    template["subHeading"]["textAlign"] = subHeadingAlignment

    if isHorizontal:
        heading_container_styles_input = input(
            "Enter headingContainer styles (width, height): "
        )
        heading_container_styles_values = heading_container_styles_input.split(" ")
        heading_width = add_px_if_integer(heading_container_styles_values[0])
        heading_height = add_px_if_integer(heading_container_styles_values[1])
        template["headingContainer"].update(
            {"width": heading_width, "height": heading_height}
        )

        subheading_container_styles_input = input(
            "Enter subHeadingContainer styles (width, height): "
        )
        subheading_container_styles_values = subheading_container_styles_input.split(
            " "
        )
        subheading_width = add_px_if_integer(subheading_container_styles_values[0])
        subheading_height = add_px_if_integer(subheading_container_styles_values[1])
        template["subHeadingContainer"].update(
            {"width": subheading_width, "height": subheading_height}
        )

        template["textContainer"]["flexDirection"] = "row"
        template["textContainer"]["justifyContent"] = "space-between"
        template["textContainer"].pop("gap")
        horizontal = input("Is text container horizontal? (y/n): ")
        
        # Optional?
        # Comment these lines if heading and subheading are not in the same line, if they are diagonally arranged

        template["textContainer"]["height"] = "100%"
        template["textContainer"]["alignItems"] = "center"
        template["textContainer"].pop("top")

    config["properties"] = template

    with open(fileName, "w") as file:
        json.dump(config, file, indent=4)

    print(f"Template saved as {fileName}")
