# Chalo [![Build Status](https://travis-ci.org/ravipunj/Chalo.svg?branch=master)](https://travis-ci.org/ravipunj/Chalo)
Chalo is a vacation discovery software that periodically builds travel plans to satisfy criteria inputted and ranks them.


## Initial Setup
1. Install Python 2.7
2. Upgrade pip: ```pip install --upgrade pip```
3. Install virtualenv: ```pip install virtualenv```
4. Clone repository: ```git clone https://github.com/ravipunj/Chalo.git```
5. Setup Virtualenv
  * ```cd Chalo```
  * ```virtualenv cenv```
  * ```source cenv/bin/activate```
  * ```pip install -r requirements.txt```

## Bash Aliases
Add these to your ~/.bash_profile

```bash
export CHALO_ROOT="~/dev/Chalo"
alias chalo="cd $CHALO_ROOT;source cenv/bin/activate;"
alias chalo-savereqs="cd $CHALO_ROOT;source cenv/bin/activate;pip freeze > requirements.txt;"
alias chalo-loadreqs="cd $CHALO_ROOT;source cenv/bin/activate;pip install -r requirements.txt;"
```

## Common Workflows
#### Adding third-party python module using pip
```bash
chalo
pip install <options> <module name>
chalo-savereqs
```