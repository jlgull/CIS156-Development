
mailing_label_data_list = [
                'Tracy Baker\n',
                'Estrella Mountain Community College\n',
                'Estrella Hall, EST N224\n',
                '3000 N. Dysart Road\n',
                'Avondale, AZ 85392\n',
                '\n\n',
                '\t\t\t',
                'name_place_holder[7]',
                '\n\t\t\t',
                'street_place_holder[9]',
                '\n\t\t\t',
                'city_place_holder[11]',
                ', ',
                'state_place_holder[13]',
                ' ',
                'postal_code_place_holder[15]',
                '\n'
                ]


# this function is used to check the input of the required fields
def get_mailing_label_info(txt):

    while True:
        data_input = input(f'{txt}')

        if data_input == '':
            print('\nThis field may not be blank. Please enter the information.\n')
        else:
            return data_input


# preabmle
print('\n\nThis program will create a mailing label and save it')
print('in a file, in the present working directory, called mailing_label.txt')

# collect addressee information
print('\nBut first, I need some information:\n')
   
mailing_label_data_list[7] = get_mailing_label_info('What is the name of the person receiving the letter? : ')
mailing_label_data_list[9] = get_mailing_label_info('What is the house / apartment number and street?     : ')
mailing_label_data_list[11] = get_mailing_label_info('What is the city?                                    : ')
mailing_label_data_list[13] = get_mailing_label_info('What is the state / province?                        : ')
mailing_label_data_list[15] = get_mailing_label_info('What is the ZIP / postal code?                       : ')    

# open the mailing_label.txt file, write all information, close file
mailing_labelelope_file = open('mailing_label.txt', 'w')
    
for i in range(len(mailing_label_data_list)):
    mailing_labelelope_file.write(mailing_label_data_list[i])

mailing_labelelope_file.close()

print('\nDisplaying mailing label:\n\n')
file_data = open('mailing_label.txt')
text = file_data.read()
file_data.close()
print(text)

print('\n\nThanks for using my program!')
