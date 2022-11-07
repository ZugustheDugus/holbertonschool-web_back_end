import * as redis from 'redis';
import { createClient } from "redis";

const client = createClient({
  host: "localhost",
});

client.on('connect', () => {
  console.log('Redis client connected to the server')
  main();
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    console.log(message);
  }
  if (message === 'KILL SERVER') {
    client.unsubscribe();
    client.quit();
  }
});

client.subscribe('holberton school channel');