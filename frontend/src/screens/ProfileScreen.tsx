import React, { useState } from 'react';
import { View, Text, Image, TouchableOpacity, StyleSheet, Alert } from 'react-native';
import { launchImageLibrary } from 'react-native-image-picker';
import Icon from 'react-native-vector-icons/Ionicons';
import CustomTextInput from '../components/CustomTextInput';
import { useNavigation } from '@react-navigation/native';
import CustomButton from '../components/CustomButton';


const ProfileScreen = () => {
  const [avatar, setAvatar] = useState(null);
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');

  const navigation = useNavigation();

  const save = () => {
    // Perform save logic here
    navigation.navigate('Home');
    console.log('Saved:', { firstName, lastName, avatar });
  }

  // Function to handle avatar upload
  const pickImage = () => {
    launchImageLibrary(
      {
        mediaType: 'photo',
        maxWidth: 300,
        maxHeight: 300,
        quality: 1,
      },
      (response) => {
        if (response.didCancel) {
          Alert.alert('You cancelled image selection');
        } else if (response.error) {
          Alert.alert('Error:', response.error);
        } else {
          const source = { uri: response.assets[0].uri };
          setAvatar(source);
        }
      }
    );
  };

  return (
    <View style={styles.container}>
      {/* Avatar Section */}
      <TouchableOpacity onPress={pickImage}>
        <View style={styles.avatarContainer}>
          {avatar ? (
            <Image source={avatar} style={styles.avatar} />
          ) : (
            <View style={styles.avatarPlaceholder}>
              {/* Default avatar icon */}
              <Image
                source={require('../assets/images/avatar.png')} // Use your default avatar image
                style={styles.avatarIcon}
              />
            </View>
          )}
          {/* Plus icon at the bottom right */}
          <View style={styles.plusIconContainer}>
            <Icon name="add-circle" size={24} color="#375FFF" />
          </View>
        </View>
      </TouchableOpacity>


      <CustomTextInput
        value={firstName}
        onChangeText={setFirstName}
        placeholder="First Name (Required)"
        keyboardType="default"
        style={styles.input}
        autoFocus={true}  // Open the keyboard by default
      />

      <CustomTextInput
        value={lastName}
        onChangeText={setLastName}
        placeholder="Last Name (Required)"
        keyboardType="default"
        style={styles.input}
      />

      {/* Save Button */}
      <CustomButton
        title="Save"
        onPress={save}
        style={styles.button}
        />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f1828',
    alignItems: 'center',
    paddingTop: 140,
  },
  avatarContainer: {
    marginBottom: 40,
    alignItems: 'center',
    justifyContent: 'center',
  },
  avatarPlaceholder: {
    width: 100,
    height: 100,
    backgroundColor: '#152033',
    borderRadius: 50,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'black',
  },
  avatarIcon: {
    width: 120,
    height: 100,
    borderRadius: 50,
    
    
  },
  plusIconContainer: {
    position: 'absolute',
    bottom: -5,
    right: -5,
  },
  avatar: {
    width: 100,
    height: 100,
    borderRadius: 50,
  },
  input: {
    width: '90%',
    
    backgroundColor: '#152033',
    borderRadius: 10,
    paddingHorizontal: 0,
    marginBottom: 0,
    fontSize: 20,
  },
  button: {
    width: '90%',
    height: 50,
    backgroundColor: '#375FFF',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 50,
    marginTop: 80,
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 18,
  },
});

export default ProfileScreen;
