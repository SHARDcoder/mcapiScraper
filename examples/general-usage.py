import mcapi

print(mcapi.query().get_status('mc.hypixel.net'))
print(mcapi.query().get_version('mc.hypixel.net'))
print(mcapi.query().get_onlinePlayers('mc.hypixel.net'))
print(mcapi.query().get_maxPlayers('mc.hypixel.net'))
