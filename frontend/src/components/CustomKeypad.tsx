import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, StyleProp, ViewStyle } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

interface KeypadProps {
  onPressKey: (key: string) => void;
  onDelete: () => void;
  style?: StyleProp<ViewStyle>;
}

const Keypad: React.FC<KeypadProps> = ({ onPressKey, onDelete, style }) => {
  const keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '', '0'];

  return (
    <View style={[styles.container, style]}>
      {keys.map((key) => (
        <TouchableOpacity
          key={key}
          style={styles.key}
          onPress={() => onPressKey(key)}
        >
          <Text style={styles.keyText}>{key}</Text>
        </TouchableOpacity>
      ))}
      <TouchableOpacity style={styles.deleteKey} onPress={onDelete}>
        <Icon name="backspace-outline" size={24} color="#fff" />
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    width: '100%', // Adjust width based on your requirements
    alignSelf: 'center',
    backgroundColor: '#152033', // Dark background to match the style
    borderRadius: 10,
    paddingVertical: 0,
  },
  key: {
    width: '30%',
    aspectRatio: 1, // Makes the button square
    justifyContent: 'center',
    alignItems: 'center',
    margin: '1.5%',
  },
  keyText: {
    fontSize: 24,
    color: '#fff',
  },
  deleteKey: {
    width: '30%',
    aspectRatio: 1,
    justifyContent: 'center',
    alignItems: 'center',
    margin: '1.5%',
  },
});

export default Keypad;
