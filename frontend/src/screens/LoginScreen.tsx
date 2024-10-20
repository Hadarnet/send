import React from 'react';
import { View, StyleSheet } from 'react-native';
import CustomTextInput from '../components/CustomTextInput';
import CustomButton from '../components/CustomButton';
import Header from '../components/Header';

const LoginScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      <Header title="Login" />
      <CustomTextInput placeholder="Email" />
      <CustomTextInput placeholder="Password" secureTextEntry />
      <CustomButton title="Login" onPress={() => { /* Handle login */ }} />
      <CustomButton 
        title="Don't have an account? Sign Up"
        onPress={() => { /* Navigate to Sign Up */ }} 
        style={styles.signupButton}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#5B2E91', // Dark purple background
    justifyContent: 'center',
    padding: 20,
  },
  signupButton: {
    marginTop: 20,
    backgroundColor: '#A52BE0', // Lighter purple for contrast
  },
});

export default LoginScreen;
