Repository demonstrating how Quarto can be installed on a Streamlit community cloud instance and used for generation of downloadable reports based on inputs or things that run on the community cloud.

Based off work done [here](https://github.com/Bergam0t/Project_Toy_MECC) - the commit history of this repo may prove useful if trying to refactor or alter approach as there is a lot there about what *didn't* work.

Code for generation of a Quarto report by first saving user inputs to a JSON: credit to [Dom Rowney](https://github.com/DomRowney), Luke Herbert and Sam Vautier for their work on generating a Quarto report for the [Toy MECC app](https://github.com/DomRowney/Project_Toy_MECC).

## Key learnings from this process

- quarto/quarto-cli not available as standard package so unable to install via adding to packages.txt

- as we don't have admin rights on streamlit community cloud server, we can't download the deb package and install with sudo dpkg -i (and running without sudo fails)

- by installing wget in packages.txt we can then download the quarto tarball and unzip that - but need to ensure it is either extracted to someone on PATH, or its location is added to PATH, so it is found
