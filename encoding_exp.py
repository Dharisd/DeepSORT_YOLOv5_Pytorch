import io
import base64


f = open("test.png","rb")


t = io.BytesIO(f.read())


data = base64.b64encode(t.getvalue())

print(data)