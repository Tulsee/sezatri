
import jwt

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imd5cHN5IiwiZXhwIjoxNTk1NjY0MDEzLCJlbWFpbCI6Imd5cHN5QGdtYWlsLmNvbSJ9.lzgVHv8365uaVFcGh5StB9uuqvl45wYdNtC4Dz8YIaw"
decoded = jwt.decode(token, verify=False)
print(decoded)
print(decoded['user_id'])
print(decoded['email'])


# import base64
# code = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk1NjYyMDIzLCJqdGkiOiI2MDAyYmZjNDU3M2Q0ODhkODMwNzIwOGU1ZmRiYzA2MyIsInVzZXJfaWQiOjF9.5LMqYZO2Sg65Mfzz3gIMOYq_iu_mrK3W4tXwGt_JSHA"

# # Ver
# token = base64.b64decode(code)
# print(token)


# # from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
# # from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

# # import jwt
# # print(token.decode("latin-1"))
# # print(token.user_id)
# # print(token["user_id"])
# # print(token[2])
# # HS256


# # valid_data = VerifyJSONWebTokenSerializer().validate(code)

# # print(valid_data['username'])
