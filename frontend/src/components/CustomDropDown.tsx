import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Modal,
  FlatList,
  StyleProp,
  ViewStyle,
  TextStyle,
} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

export interface DropdownOption {
  label: string; // Country name
  value: any; // Unique identifier for the option
  code: string; // Country code
  flag: string; // Country flag
}

interface CustomDropdownProps {
  label?: string;
  selectedValue?: DropdownOption;
  onValueChange: (item: DropdownOption) => void;
  options: DropdownOption[];
  placeholder?: string;
  style?: StyleProp<ViewStyle>;
  dropdownStyle?: StyleProp<ViewStyle>;
  textStyle?: StyleProp<TextStyle>;
}

const CustomDropdown: React.FC<CustomDropdownProps> = ({
  label,
  selectedValue,
  onValueChange,
  options,
  placeholder = 'Select an option',
  style,
  dropdownStyle,
  textStyle,
}) => {
  const [visible, setVisible] = useState<boolean>(false);

  const handleSelect = (item: DropdownOption) => {
    onValueChange(item);
    setVisible(false);
  };

  return (
    <View style={[styles.container, style]}>
      {label && <Text style={styles.label}>{label}</Text>}
      <TouchableOpacity
        style={[styles.dropdown, dropdownStyle]}
        onPress={() => setVisible(true)}
        activeOpacity={0.7}
      >
        <Text style={[styles.text, textStyle]}>
          {selectedValue ? `${selectedValue.flag} ${selectedValue.code}` : placeholder}
        </Text>
        <Icon name="chevron-down" size={20} color="#5A2A83" />
      </TouchableOpacity>

      <Modal visible={visible} transparent animationType="slide">
        <TouchableOpacity style={styles.modalOverlay} activeOpacity={1} onPress={() => setVisible(false)}>
          <View style={styles.modalContent}>
            <FlatList
              data={options}
              keyExtractor={(item) => item.value ? item.value.toString() : Math.random().toString()} // Fallback to random string for unique keys
              renderItem={({ item }) => (
                <TouchableOpacity
                  style={styles.option}
                  onPress={() => handleSelect(item)}
                  activeOpacity={0.7}
                >
                  <Text style={styles.optionText}>
                    {item.flag} {item.code} {item.label}
                  </Text>
                </TouchableOpacity>
              )}
            />
          </View>
        </TouchableOpacity>
      </Modal>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginVertical: 10,
    width: '30%',
  },
  label: {
    marginBottom: 5,
    color: '#fff',
    fontSize: 16,
  },
  dropdown: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#3A0078',
    padding: 15,
    borderRadius: 8,
  },
  text: {
    color: '#fff',
    fontSize: 16,
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.5)',
    justifyContent: 'center',
    padding: 20,
  },
  modalContent: {
    backgroundColor: '#fff',
    borderRadius: 8,
    maxHeight: '80%',
  },
  option: {
    padding: 15,
    borderBottomWidth: 1,
    borderBottomColor: '#ddd',
  },
  optionText: {
    fontSize: 16,
    color: '#333',
  },
});

export default CustomDropdown;
