import ballerina/http;
import ballerina/log;

final record {
    float temperatura;
    float humedad;
} sensorData = {temperatura: 0.0, humedad: 0.0};

service /sensor  on new http:Listener(8080) {

resource function post data(http:Caller caller, http:Request req) returns error? {

json sensorData = check req.getJsonPayload();
log:printInfo("Datos recibidos del sensor: "+sensorData.toString());


check caller->respond("Datos recibidos correctamente.");

}

resource function get data(http:Caller caller) returns error? {
        check caller->respond(sensorData);
    }


}
