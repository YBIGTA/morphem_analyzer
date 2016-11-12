
readonly PROG_NAME=$(basename $0)
readonly PROG_DIR=$(readlink -m $(dirname $0))


cp $PROG_DIR/web_toon_user_dictionary/* $PROG_DIR/mecab-ko-dic-2.0.1-20150920/
#bash mecab-ko-dic-2.0.1-20150920/tools/add-userdic.sh
cd $PROG_DIR/mecab-ko-dic-2.0.1-20150920
#sudo make clean
#sudo make install
make clean
make install
cd ..
