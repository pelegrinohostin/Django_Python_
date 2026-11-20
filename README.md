Códigos de Estado HTTP
1xx - Informativos
Código	Significado
100	Continue
101	Switching Protocols
2xx - Éxito
Código	Significado
200	OK
201	Created
202	Accepted
204	No Content
Ejemplos
HTTP/1.1 200 OK
HTTP/1.1 201 Created
3xx - Redirecciones
Código	Significado
301	Moved Permanently
302	Found
304	Not Modified
Ejemplo
HTTP/1.1 301 Moved Permanently
Location: https://ejemplo.com
4xx - Error del cliente
Código	Significado
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
405	Method Not Allowed
429	Too Many Requests
Ejemplos
HTTP/1.1 404 Not Found
HTTP/1.1 403 Forbidden
5xx - Error del servidor
Código	Significado
500	Internal Server Error
502	Bad Gateway
503	Service Unavailable
504	Gateway Timeout
Ejemplos
HTTP/1.1 500 Internal Server Error
HTTP/1.1 503 Service Unavailable
Los más importantes para desarrollo web
✅ 200 OK
✅ 201 Created
✅ 301 Moved Permanently
✅ 400 Bad Request
✅ 401 Unauthorized
✅ 403 Forbidden
✅ 404 Not Found
✅ 500 Internal Server Error

Comprobar respuestas HTTP con curl
curl -I https://www.google.com
curl -X GET https://api.ejemplo.com
curl -X POST https://api.ejemplo.com/usuarios