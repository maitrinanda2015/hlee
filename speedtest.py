from speedtest import Speedtest
st = Speedtest()
print("your connection's Download speed is :",st.download())
print("Your connection's Upload speed is :",st.upload())