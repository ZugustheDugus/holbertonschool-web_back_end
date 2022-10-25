// Displays welcome message and asks for name, then displays users
// input name

console.log('Welcome to Holberton School, what is your name?');
process.stdin
  .on('readable', () => {
    const name = process.stdin.read();
    if (name) {
      process.stdout.write(`Your name is: ${name}`);
    }
  })
  .on('end', () => {
    console.log('This important software is now closing');
  });
