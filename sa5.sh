clear
blue='\033[34;1m'
green='\033[32;1m'  
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'                                           
yellow='\033[33;1m'
clear
sleep 1
toilet "S.A" -F metal
echo $green"_____________________________"
echo $red"Hello welcome tool S.A-5 bpc"
echo $red"          |WARNING|      "
echo $green"TOOL INI HANYA BOLEH DI GUNAKAN"
echo $green"SAAT KEADAAN TERDESAK"
echo $green"UNTUK MENJALANKAN MEMERLUKAN"
echo $green"KODE KHUSUS"
echo $green"_____________________________"
echo
echo $red"MASUKAN KODE TOOL"
read -p ">>>>> " D721;
sleep 1
echo $cyan"MEMERIKSA KODE $D721"
sleep 6
toilet "KODE SALAH" 
echo
echo
if [ $D721 = D721 ] || [ $D721 = D721 ]
then
clear
toilet "KODE BENAR" -F metal
echo
sh main.sh
fi
