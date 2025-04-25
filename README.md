# mcrc-cetuximab-analysis

Анализ молекулярных механизмов резистентности связанных с выживаемостью и ответом на терапию цетуксимабом среди пациентов страдающих от метастатического колоректального рака

Цель работы
Понять, какие молекулярные механизмы могут быть связаны с выживаемостью и ответом на терапию цетуксимабом у пациентов с метастатическим колоректальным раком (мКРР). Особое внимание будет уделено роли гена MET, активности сигнальных путей MAPK и PI3K, а также эпителиально-мезенхимальному переходу (EMT).


# SETUP INSTRUCTIONS

        curl https://pyenv.run | bash

Add to .bashrc: 

        export PATH="$HOME/.pyenv/bin:$PATH"
        eval "$(pyenv init --path)"
        eval "$(pyenv init -)"

Then:

        pyenv install 3.12.0
        pyenv global 3.12.0 

        cd YOUR_REPO_DIR
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt