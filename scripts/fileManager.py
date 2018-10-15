import getpass

class FileManager:
    __user_name = getpass.getuser()
    __order_path = "/home/" + __user_name + "/Documents/"

    def __init__(self, settingsManager):
        self.__settingsManager = settingsManager
        self.__order_path = self.__order_path + self.__settingsManager.get_settings()['order_name'] + "txt"

    def __get_file_string(self, date, hours, note):
        return date + ":  " + (" " + str(hours) if hours < 10 else str(hours)) \
               + "h" + ((", Note: " + note) if note != "" else "")

    def save_order(self, data_list):
        with open(self.__order_path, "w") as file:
             for item in data_list:
                 file.write(self.__get_file_string(item[0], item[1], item[2]) + "\n")

    def get_order_path(self):
        return self.__order_path


