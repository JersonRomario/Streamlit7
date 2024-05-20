import streamlit as st
from collections import Counter
import io

def read_log_file(file):
    errors = []
    for line in file:
        line_text = line.decode("utf-8").strip()
        if line_text.startswith("ERROR"):
            errors.append(line_text)
    error_counts = Counter(errors)
    return error_counts

def save_summary(error_counts):
    output = io.StringIO()
    for error, count in error_counts.items():
        output.write(f"{error}: {count}\n")
    return output.getvalue().encode('utf-8')

def main():
    st.title("Resumen de Errores en Archivo de Log")

    uploaded_file = st.file_uploader("Sube tu archivo de log (TXT)", type=["txt"])

    if uploaded_file is not None:
        st.write("Archivo cargado:")
        st.text(uploaded_file.name)

        error_counts = read_log_file(uploaded_file)

        st.write("Resumen de errores:")
        for error, count in error_counts.items():
            st.write(f"{error}: {count}")

        save_button = st.button("Guardar resumen en archivo")

        if save_button:
            output = save_summary(error_counts)
            st.download_button(label="Descargar resumen",
                               data=output,
                               file_name="resumen_errores.txt",
                               mime="text/plain")
            st.success("Archivo guardado con éxito como 'resumen_errores.txt'.")

if __name__ == "__main__":
    main()
