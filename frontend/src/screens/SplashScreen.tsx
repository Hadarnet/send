import React from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';
import CustomButton from '../components/CustomButton'; // Import your custom button component
import { useNavigation } from '@react-navigation/native';

const SplashScreen: React.FC = () => {

    const navigation = useNavigation();

  const handleStartMessaging = () => {
    navigation.navigate('Signup');
  };

  return (
    <View style={styles.container}>
      <Image
        source={require('../assets/images/Illustration.png')} // Ensure the path is correct
        style={styles.image}
        resizeMode="contain"
      />
      <Text style={styles.title}>Connect easily with your family and friends over countries</Text>
      
      

      <Text style={styles.terms}>Terms & Privacy Policy</Text>

      <CustomButton
        title="Start Messaging"
        onPress={handleStartMessaging}
        
        iconPosition="left"
        style={styles.button}
        textStyle={styles.buttonText}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0f1828', // Dark purple background
    paddingTop: 50,
    
  },
  image: {
    width: '100%',
    height: 320, // Adjust based on your needs
    marginBottom: 30,
  },
  title: {
    fontSize: 29,
    color: '#FFFFFF', // White text
    textAlign: 'center',
    marginBottom: 0,
    fontWeight: '700',
    lineHeight: 38,
    width: '90%', // Customize the width as needed
    fontFamily: 'Mulish-Bold'
    
  },
  button: {
    width: '80%', // Customize the button width
    marginTop: 10,
    backgroundColor: '#375FFF',
    borderRadius: 50, // Rounded corners
    padding: 15,
    fontFamily: 'Mulish-Regular'
  },
  buttonText: {
    fontSize: 18,
  },
  terms: {

    fontSize: 18,
    textAlign: 'center',
    marginTop: '40%',
    color: '#FFFFFF',
    fontFamily: 'Mulish-Regular',
    lineHeight: 24,
    marginBottom: 4,
  },
});

export default SplashScreen;
