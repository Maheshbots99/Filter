if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Maheshbot99/Filter.git /Filter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Filter
fi
cd /Filter
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
