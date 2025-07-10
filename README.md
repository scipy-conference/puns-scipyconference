# puns-scipyconference

Making the T-shirt puns work!

Made with ❤️ by the SciPy Conference Organizers.

## Installation

### Basic installation (community-curated puns only)
```bash
pip install scipyconference
```


## Contributing

### Our vision

The idea behind this package is to collectively create and serve our own puns! We want to make it super simple and easy for people to contribute. We envision this as something that somebody could use to load historic puns from various SciPy conference archives that people submit and create at the conference.

Our goal is to maintain minimal dependencies and scaffolding to ensure we can get as many contributions as possible while keeping the barrier to entry low.

### How to contribute puns

Contributing new puns is simple! Just edit the `scipyconference/puns.json` file and add your pun to the collection. The file contains a JSON array of pun objects - add yours following the same format.
Adding your GitHub handle for pun attribution is optional.

## Get started for development

To contribute new puns:

1. Fork this repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone git@github.com:YOUR_USERNAME/puns-scipyconference.git
   cd puns-scipyconference
   ```
3. Create a new branch for your puns:
   ```bash
   git checkout -b add-my-puns
   ```
4. Edit `scipyconference/puns.json` with your favorite editor:
   ```bash
   # Using nano
   nano scipyconference/puns.json

   # Using vim
   vim scipyconference/puns.json

   # Using emacs
   emacs scipyconference/puns.json
   ```
5. Save your changes, and then commit and push your changes:
   ```bash
   git add scipyconference/puns.json
   git commit -m "Add new puns for SciPy conference"
   git push origin add-my-puns
   ```
6. Create a pull request from your fork's `add-my-puns` branch to the main repository's `main` branch
