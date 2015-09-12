# reederz.com

Powered by [Pelican](http://docs.getpelican.com/en/3.6.0/) and hosted on [GitHub Pages](https://pages.github.com/).

```bash
# Setup requirements
virtualenv --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt

# Download themes and plugins
git clone --recursive https://github.com/getpelican/pelican-themes ../pelican-themes
wget -O ../pelican-themes/voidy-bootstrap/static/css/bootstrap.min.css https://bootswatch.com/cosmo/bootstrap.min.css
git clone --recursive https://github.com/getpelican/pelican-plugins ../pelican-plugins

# Build an run
make html
make devserver
```
