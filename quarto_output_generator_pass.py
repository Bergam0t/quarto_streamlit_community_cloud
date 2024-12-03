import streamlit as st
import json
import os
import subprocess

st.session_state.download_clicked = False

st.title("Passing Parameters to a Quarto Template")

st.write(
    """
In this example, the inputs from the user are saved in a json file and this is then accessed
by quarto when rendering the document.
    """
)

first_number_input = st.slider("Enter a first number", 1, 100)

second_number_input = st.number_input("Enter a second number")

operation_input = st.selectbox(
    "Select an operation",
    ["Add", "Subtract", "Multiply", "Divide"]
    )

def disable_download():
    st.session_state.download_clicked = True
    report_message.empty()

if st.button("Generate Output"):

    json_path = os.path.join(os.getcwd(), 'session_data.json')
    print(json_path)

    model_parameters = {
        "input_1": first_number_input,
        "input_2": second_number_input,
        "operation": operation_input
    }

    with open(json_path, "w") as f:
        json.dump(model_parameters, f)

    report_message = st.empty()

    report_message.info("Generating Report...")

    ## filepaths for
    output_dir = os.path.join(os.getcwd(),'outputs')
    qmd_filename = 'quarto_calculator_output.qmd'
    qmd_path = os.path.join(os.getcwd(),qmd_filename)
    html_filename = os.path.basename(qmd_filename).replace('.qmd', '.html')
    dest_html_path = os.path.join(output_dir,html_filename)

    try:
        ## forces result to be html
        result = subprocess.run(["quarto"
                                , "render"
                                , qmd_path
                                , "--to"
                                , "html"
                                , "--output-dir"
                                , output_dir]
                                , capture_output=True
                                , text=True)
    except:
        ## error message
        report_message.error(f"Report cannot be generated")

    if os.path.exists(dest_html_path):
        with open(dest_html_path, "r") as f:
            html_data = f.read()

        report_message.success("Report Available for Download")

        if not st.session_state.download_clicked:
            st.download_button(
                label="Download Report",
                data=html_data,
                file_name=html_filename,
                mime="text/html",
                # disabled=not st.session_state.simulation_completed,
                on_click=disable_download
            )
    else:
        ## error message
        report_message.error(f"Report failed to generate\n\n_{result}_")

else:
    ## empty location for report message
    report_message = st.empty()
