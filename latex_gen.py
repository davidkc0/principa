import os

# Path to the folder containing images
folder = "figures/ofig/"

# Supported image extensions
extensions = ('.png', '.jpg', '.jpeg', '.pdf', '.JPG')



# Generate LaTeX code
def gen_code(folder, file):
    latex_code = """\\begin{figure}
        \centering
        \includegraphics[width=0.8\\textwidth]{"""+"{}/{}".format(folder, file)+"""}
    \end{figure}
    """
    latex_code = latex_code.replace("//", "/")
    return latex_code

for file in sorted(os.listdir(folder)):
    if file.endswith(extensions):
        print(gen_code(folder, file))

#print(latex_code)
