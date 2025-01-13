import subprocess

def install_libraries():
    libraries = [
        "matplotlib",
        "shapely",
        "numpy",
        "scipy",
        "pandas",
        "sympy",
        "scikit-learn",
        "tensorflow",
        "torch",
        "keras",
        "xgboost",
        "seaborn",
        "plotly",
        "networkx",
        "pytorch-lightning",
        "jupyterlab",
        "notebook",
        "ipywidgets",
        "pymc3",
        "arviz",
        "statsmodels",
        "openai",
        "transformers",
        "datasets",
        "nltk",
        "spacy",
        "gensim",
        "umap-learn",
        "h5py",
        "tqdm",
        "cvxpy",
        "pulp",
        "geopandas",
        "folium",
        "dash",
        "bokeh",
        "mayavi",
        "fastai",
        "lightgbm",
        "catboost",
        "mlxtend",
        "joblib",
        "optuna",
        "pydot",
        "graphviz",
        "pyomo",
        "shap",
        "lime",
        "pydeck",
        "pyvis"
    ]

    for library in libraries:
        try:
            print(f"Installing {library}...")
            subprocess.check_call(["pip", "install", library])
        except subprocess.CalledProcessError as e:
            print(f"Error installing {library}: {e}")

if __name__ == "__main__":
    install_libraries()
