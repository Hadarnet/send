import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  Modal,
  TouchableOpacity,
  StyleProp,
  ViewStyle,
  TextStyle,
} from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';

interface ModalComponentProps {
  visible: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
  containerStyle?: StyleProp<ViewStyle>;
  titleStyle?: StyleProp<TextStyle>;
  bodyStyle?: StyleProp<ViewStyle>;
}

const ModalComponent: React.FC<ModalComponentProps> = ({
  visible,
  onClose,
  title,
  children,
  containerStyle,
  titleStyle,
  bodyStyle,
}) => {
  return (
    <Modal visible={visible} transparent animationType="fade">
      <TouchableOpacity style={styles.overlay} activeOpacity={1} onPress={onClose}>
        <View style={[styles.modalContent, containerStyle]}>
          <View style={styles.header}>
            <Text style={[styles.title, titleStyle]}>{title}</Text>
            <TouchableOpacity onPress={onClose} activeOpacity={0.7}>
              <Icon name="close" size={24} color="#5A2A83" />
            </TouchableOpacity>
          </View>
          <View style={[styles.body, bodyStyle]}>{children}</View>
        </View>
      </TouchableOpacity>
    </Modal>
  );
};

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.5)',
    justifyContent: 'center',
    padding: 20,
  },
  modalContent: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 20,
    maxHeight: '80%',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  title: {
    fontSize: 18,
    color: '#5A2A83',
    fontWeight: 'bold',
  },
  body: {
    marginTop: 20,
  },
});

export default ModalComponent;
