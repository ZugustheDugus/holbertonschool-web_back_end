import { createClient } from "redis";
import * as redis from 'redis';
import promisify from 'util';

const promisify = require('util').promisify;

const client = createClient({
  host: "localhost",
});

client.on('connect', () => {
  console.log('Redis client connected to the server')
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, redis.print);
}

const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.GET).bind(client)(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');