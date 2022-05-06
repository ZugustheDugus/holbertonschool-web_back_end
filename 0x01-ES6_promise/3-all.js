import { uploadPhoto, createUser } from './utils';

export default function handleProfilesSignup () {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      console.log('${values[0].body}, ${values[1].firstName}, ${values[2].lastName}');
    }).catch(() => {
      console.log('Signup system offlin');
    });
}
