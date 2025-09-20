# Importando o Speedtest
import speedtest as st

speed = st.Speedtest()
download = f"{'{:.2f}'.format(speed.download()/1024/1024)}"
upload = f"{'{:.2f}'.format(speed.upload()/1024/1024)}"

print(download)
print(upload)