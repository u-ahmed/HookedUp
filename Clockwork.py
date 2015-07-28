#############
# clockwork #
#############

from clockwork import clockwork

api = clockwork.API('146ac839459530e7910f2613900c07c845aec86b')
message = clockwork.SMS(to = "447455968412", message = "Test")
response = api.send(message)

if response.success:
    print(response.id)
else:
    print(response.error_code)
    print(response.error_description)
