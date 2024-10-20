import React, { useState } from 'react';
import { View, Text, StyleSheet, Alert } from 'react-native';
import { countries } from '../assets/data/countries'; // Import the countries array

import Keypad from '../components/CustomKeypad';
import CustomDropdown, { DropdownOption } from '../components/CustomDropDown';
import CustomTextInput from '../components/CustomTextInput';
import CustomButton from '../components/CustomButton';
import { useNavigation } from '@react-navigation/native';
import { StackNavigationProp } from '@react-navigation/stack';
import { RootStackParamList } from '../navigation/types';


type SignupScreenNavigationProp = StackNavigationProp<RootStackParamList, 'Signup'>;

const SignupScreen: React.FC = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedCountry, setSelectedCountry] = useState<DropdownOption>(countries[0]); // Default selection

  const navigation = useNavigation<SignupScreenNavigationProp>();

  const handleKeyPress = (key: string) => {
    setInputValue((prev) => prev + key);
  };

  const handleDelete = () => {
    setInputValue((prev) => prev.slice(0, -1));
  };

  const handleSignUp = () => {
    // Your signup logic here
    navigation.navigate('OtpScreen', {
      phoneNumber: `${selectedCountry.code}${inputValue}`,
      
    });
    console.log(`${selectedCountry.code}${inputValue}`);
  };
    
  

  return (
    <View style={styles.container}>
      <View style={styles.contentContainer}>
        <Text style={styles.Title}>
          Enter Your Phone Number
        </Text>
        <Text style={styles.subTitle}>
          Please confirm your country code and enter your phone number
        </Text>
        <View style={styles.rowContainer}>
  <CustomDropdown
    selectedValue={selectedCountry}
    onValueChange={setSelectedCountry}
    options={countries}
    dropdownStyle={styles.dropdownStyle}
  />

  <CustomTextInput
    value={inputValue}
    onChangeText={setInputValue}
    placeholder="Phone Number"
    keyboardType="numeric"
    style={styles.inputField}  // Apply styling to the input field
  />
</View>

<CustomButton
        title="Continue"
        onPress={handleSignUp}
        
        
        iconPosition="left"
        style={styles.button}
        textStyle={styles.buttonText}
      />


        
        
        {/* Adjust Keypad visibility */}
        <Keypad onPressKey={handleKeyPress} onDelete={handleDelete} />

        
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f1828',
    
    
  },
  contentContainer: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  inputText: {
    fontSize: 32,
    color: '#fff',
    marginBottom: 20,
  },
  Title: {
    color: '#fff',
    fontSize: 28,
    marginBottom: 10,
    marginTop: '40%',
  },
  subTitle: {
    color: '#fff',
    fontSize: 16,
    marginBottom: 20,
    textAlign: 'center',
    width: '80%',
    lineHeight: 24,
  },
  button: {
    marginTop: 90,
    backgroundColor: '#375FFF',
    borderRadius: 50,
    width: '80%',
    height: 50,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 50,
    
    
    
    
  },
  buttonText: {
    
    
    
     
    
    fontFamily: 'Mulish-Regular',
    alignItems: 'center',
    justifyContent: 'center',
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  
  inputa:{
    width: '20%',
    flex:1
    
    
  },
 
  flexContainer: {
    flexDirection: 'row', // Aligns children in a row
    marginBottom: 120,
    
 
    // Adjusts space between items
    
  },
  rowContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    width: '90%', // Wider width for better space distribution
    marginBottom: 20,
    paddingHorizontal: 10,
  },
  dropdownStyle: {
    flex: 1, // Take up available space proportional to the row
    backgroundColor: '#152033',
    borderRadius: 8,
    height: 50,
    justifyContent: 'center',
    paddingHorizontal: 10,
    marginRight: 10, // Adds space between dropdown and input field
    maxWidth: '80%',
    
  },
  inputField: {
    flex: 2, // Takes up more space relative to dropdown
    height: 50,
    backgroundColor: '#152033',
    borderRadius: 8,
    paddingHorizontal:0,
    color: '#000',
    width: '50%',
  },
  
});

export default SignupScreen;
