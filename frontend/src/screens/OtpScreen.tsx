import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Alert } from 'react-native';
import Keypad from '../components/CustomKeypad'; // Assuming you have a Keypad component
import { RouteProp, useRoute, useNavigation } from '@react-navigation/native';
import { OtpScreenRouteProp } from '../navigation/types';
import { StackNavigationProp } from '@react-navigation/stack';
import { RootStackParamList } from '../navigation/types'; // Assuming you have a type for your navigation stack

const OtpScreen: React.FC = () => {
  const [otp, setOtp] = useState<string[]>(['', '', '', '']);
  const route = useRoute<OtpScreenRouteProp>(); // Use the typed route prop
  const { phoneNumber } = route.params;
  const navigation = useNavigation<StackNavigationProp<RootStackParamList>>();

  const handleKeyPress = (key: string) => {
    const newOtp = [...otp];
    const emptyIndex = newOtp.findIndex((value) => value === '');
    if (emptyIndex !== -1) {
      newOtp[emptyIndex] = key;
      setOtp(newOtp);
    }
  };

  const handleDelete = () => {
    const newOtp = [...otp];
    const filledIndex = newOtp.findIndex((value) => value === '');
    const indexToClear = filledIndex === -1 ? newOtp.length - 1 : filledIndex - 1;
    if (indexToClear >= 0) {
      newOtp[indexToClear] = '';
      setOtp(newOtp);
    }
  };

  const handleResend = () => {
    Alert.alert('Resend Code', 'The OTP code has been resent to your number.');
  };

  // Check if OTP is 0000 and navigate to ProfileScreen
  useEffect(() => {
    if (otp.join('') === '0000') {
      navigation.navigate('ProfileScreen'); // Replace with your actual ProfileScreen route name
    }
  }, [otp]);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Enter Code</Text>
      <Text style={styles.subTitle}>
        We have sent you an SMS with the code to {phoneNumber}
      </Text>
      <View style={styles.otpContainer}>
        {otp.map((value, index) => (
          <View key={index} style={[styles.otpBox, value ? styles.otpBoxFilled : null]}>
            <Text style={styles.otpText}>{value}</Text>
          </View>
        ))}
      </View>
      <TouchableOpacity onPress={handleResend}>
        <Text style={styles.resendText}>Resend Code</Text>
      </TouchableOpacity>
      <View style={styles.keypadContainer}>
        <Keypad onPressKey={handleKeyPress} onDelete={handleDelete} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f1828',
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 0,
    paddingTop: '80%',
  },
  title: {
    color: '#fff',
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  subTitle: {
    color: '#fff',
    fontSize: 14,
    textAlign: 'center',
    marginBottom: 30,
    lineHeight: 22,
    maxWidth: '70%',
  },
  otpContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '80%',
    marginBottom: 60,
  },
  otpBox: {
    width: 55,
    height: 55,
    backgroundColor: '#152033',
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    borderColor: '#375FFF',
    borderWidth: 1,
  },
  otpBoxFilled: {
    borderColor: '#fff',
    borderWidth: 2,
  },
  otpText: {
    fontSize: 24,
    color: '#fff',
  },
  resendText: {
    color: '#fff',
    fontSize: 16,
    marginBottom: 20,
    marginTop: 80,
  },
  keypadContainer: {
    width: '100%',
    paddingTop: 10,
  },
});

export default OtpScreen;
