import React from 'react';
import {
  View,
  TextInput,
  Text,
  StyleSheet,
  TextInputProps,
  StyleProp,
  ViewStyle,
  TextStyle,
} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

interface CustomTextInputProps extends TextInputProps {
  label?: string;
  iconName?: string;
  error?: string;
  style?: StyleProp<ViewStyle>;
  inputStyle?: StyleProp<TextStyle>;
}

const CustomTextInput: React.FC<CustomTextInputProps> = ({
  label,
  placeholder,
  value,
  onChangeText,
  iconName,
  secureTextEntry = false,
  keyboardType = 'default',
  error,
  style,
  inputStyle,
  ...rest
}) => {
  return (
    <View style={[styles.container, style]}>
      {label && <Text style={styles.label}>{label}</Text>}

      <View
        style={[
          styles.inputWrapper,
          { borderColor: error ? '#FF6B6B' : '#152033' }, // Border color change on error
        ]}
      >
        {/* Icon */}
        {iconName && (
          <Icon
            name={iconName}
            size={20}
            color={error ? '#FF6B6B' : '#5A2A83'} // Change icon color on error
            style={styles.icon}
          />
        )}

        {/* Text Input */}
        <TextInput
          style={[styles.input, inputStyle]}
          placeholder={placeholder}
          placeholderTextColor="#999"
          value={value}
          onChangeText={onChangeText}
          secureTextEntry={secureTextEntry}
          keyboardType={keyboardType}
          accessible={true}
          accessibilityLabel={label || placeholder}
          {...rest}
        />
      </View>

      {/* Error Message */}
      {error && <Text style={styles.error}>{error}</Text>}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginVertical: 10,
    width: '100%',
  },
  label: {
    marginBottom: 5,
    color: '#fff',
    fontSize: 16,
  },
  inputWrapper: {
    flexDirection: 'row',
    backgroundColor: '#152033',
    borderRadius: 8,
    alignItems: 'center',
    paddingHorizontal: 10,
    borderWidth: 1, // Add a border for better focus indication
  },
  icon: {
    marginRight: 8,
  },
  input: {
    flex: 1,
    height: 50,
    color: '#fff',
    fontSize: 16, // Adjusted font size for better readability
  },
  error: {
    color: '#FF6B6B',
    marginTop: 5,
    fontSize: 14,
  },
});

export default CustomTextInput;
