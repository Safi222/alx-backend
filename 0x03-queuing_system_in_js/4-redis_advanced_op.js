import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => console.log('Redis client connected to the server'));

const myHash = {
	Portland: 50,
	Seattle: 80,
	'New York': 20,
	Bogota: 20,
	Cali: 40,
	Paris: 2,
};

Object.entries(myHash).forEach((entry) => {
	client.hset('HolbertonSchools', entry[0], entry[1], print);
});

client.hgetall('HolbertonSchools', (error, result) => {
	if (error) {
		console.log(error);
		throw error;
	}
	console.log(result);
});
