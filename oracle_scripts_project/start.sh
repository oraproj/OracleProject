echo -e "\n\n******************************************************"
echo -e "*                                                    *"
echo -e "*            Adding environments varibles            *"
echo -e "*                                                    *"
echo -e "******************************************************"
orahome=`echo ${ORACLE_HOME}`
export ORACLE_HOME=/opt/ora/instantclient_11_2
echo -e "ORACLE_HOME=$ORACLE_HOME"

oralib=`echo ${LD_LIBRARY_PATH}`
export LD_LIBRARY_PATH=/opt/ora/instantclient_11_2
echo -e "LD_LIBRARY_PATH=$LD_LIBRARY_PATH \n\n"

echo -e "\n******************************************************"
echo -e "*                                                    *"
echo -e "*     Running and installing system requirements     *"
echo -e "*                                                    *"
echo -e "******************************************************"
sudo aptitude install python-dev

echo -e "\n\n******************************************************"
echo -e "*                                                    *"
echo -e "*  Running and installing python requirements files  *"
echo -e "*                                                    *"
echo -e "******************************************************"
sudo pip install -r requirements.txt

echo -e "\n\n******************************************************"
echo -e "*                                                    *"
echo -e "*                   Running System                   *"
echo -e "*                                                    *"
echo -e "******************************************************"
echo -e "Running system"
python scripts/first_run/first_run.py
python manage.py runserver
