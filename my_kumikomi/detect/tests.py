import detect

result = detect.detect({
    "type": "msg",
    "data": "hello",
    "name": "akakou",
    "service": "line"
})

print(result)

