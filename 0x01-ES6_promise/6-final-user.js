import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup (firstName, lastName, fileName) {
  return [await signUpUser(firstName, lastName)
    .then((response) => ({ status: 'fulfilled', response }))
    .catch((err) => ({ status: 'rejected', value: err })),
  await uploadPhoto(fileName)
    .then((response) => ({ status: 'fulfilled', response }))
    .catch((err) => ({ status: 'rejected', value: err.toString() }))];
}
