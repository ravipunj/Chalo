# Chalo
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
alias chalo="cd <path_to_repo>;source cenv/bin/activate;"
```