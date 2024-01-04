import tkinter
from tkinter import ttk
import mysql.connector

class CatGenerator:
    def __init__(self):
        self.cat_id = 0

    def generate_running_number(self):
        self.cat_id += 1
        return self.cat_id

    def insert_running_number(self, cat_name, cat_breed, cat_age, cat_medcon, date, check_in, check_out, duration_hour, owner_name, phone_num, address, payment):
        cat_id = self.generate_running_number()

        sql = 'INSERT INTO cat(CAT_ID, CAT_NAME, CAT_BREED, CAT_AGE, CAT_MEDCON, DATE, CHECK_IN, CHECK_OUT, DURATION_HOUR, OWNER_NAME, PHONE_NUM, ADDRESS, PAYMENT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        val = (cat_id, cat_name, cat_breed, cat_age, cat_medcon, date, check_in, check_out, duration_hour, owner_name, phone_num, address, payment)

        try:
            cursor.execute(sql, val)
            mydb.commit()
            print('Data saved successfully.')
        except Exception as e:
            print(f'Error saving data: {e}')

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cat_daycare_centre'
)

# Create a cursor object to execute SQL queries
cursor = mydb.cursor()

# Create a global instance of CatGenerator
cat_generator = CatGenerator()

def save_data():
    try:
        cat_name = cat_name_entry.get()
        cat_breed = cat_breed_combobox.get()
        cat_age = cat_age_spinbox.get()
        cat_medcon = cat_medical_condition_combobox.get()
        date = date_entry.get()
        check_in = check_in_spinbox.get()
        check_out = check_out_spinbox.get()
        duration_hour = duration_hour_entry.get()
        owner_name = owner_name_entry.get()
        phone_num = owner_phone_num_entry.get()
        address = owner_address_entry.get()

        # Perform a calculation (e.g., square the input)
        payment = float(duration_hour_entry.get()) * 4


        # Insert data with running number
        cat_generator.insert_running_number(cat_name, cat_breed, cat_age, cat_medcon, date, check_in, check_out, duration_hour, owner_name, phone_num, address, payment)

    except Exception as e:
        print(f'Error saving data: {e}')

def perform_calculation():
    try:
        # Get the value from the Entry widget and convert it to a float
        hour = float(duration_hour_entry.get())

        # Perform a calculation
        payment = hour * 4

        # Update the result_label with the calculated result
        payment_label.config(text=f'Payment: RM {payment}')

    except ValueError:
         #Handle the case where the input is not a valid float
        payment_label.config(text='Invalid input. Please enter a number.')


root = tkinter.Tk()
root.title('Cat Information')

frame = ttk.Frame(root)
frame.grid()

cat_info_frame = ttk.LabelFrame(frame, text='Cat Information')
cat_info_frame.grid(row=0, column=0, padx=50, pady=50)

#GUI code

#cat's name
cat_name_label = tkinter.Label(cat_info_frame, text = 'Name: ')
cat_name_label.grid(row = 0, column = 0, padx=10, pady=10)
cat_name_entry = tkinter.Entry(cat_info_frame)
cat_name_entry.grid(row = 0, column = 1, padx=10, pady=10)


#cat's breed
cat_breed_label = tkinter.Label(cat_info_frame, text = 'Breed: ')
cat_breed_label.grid(row = 0, column = 2, padx=10, pady=10)
cat_breed_entry = tkinter.Entry(cat_info_frame)
cat_breed_combobox = ttk.Combobox(cat_info_frame, values =['','Siamese', 'British Shorthair', 'Maine Coon', 'Persian', 'Ragdoll', 'Sphynx', 'American Shorthair', 'Abyssinian', 'Exotic Shorthair', 'Scottish Fold', 'Burmese', 'Birman', 'Bombay', 'Devon Rex', 'Balinese', 'Javanese', 'Oriental Shorthair', 'Munchkin'])
cat_breed_combobox.grid(row = 0, column = 3, padx=10, pady=10)

#cat's age
cat_age_label = tkinter.Label(cat_info_frame, text = 'Age: ')
cat_age_label.grid(row = 0, column = 4, padx=10, pady=10)
cat_age_spinbox = tkinter.Spinbox(cat_info_frame, from_= 1, to = 20)
cat_age_spinbox.grid(row = 0, column = 5, padx=10, pady=10)

#cat's medical condition
cat_medical_condition_label = tkinter.Label(cat_info_frame, text = 'Medical condition: ')
cat_medical_condition_label.grid(row = 1, column = 0, padx=10, pady=10)
cat_medical_condition_combobox = ttk.Combobox(cat_info_frame, values = ['', 'None'])
cat_medical_condition_combobox.grid(row = 1, column = 1, padx=10, pady=10)


#reservation
#date    
date_label = tkinter.Label(cat_info_frame, text = 'Date (YYYY/MM/DD) : ')
date_label.grid(row = 3, column = 0, padx=10, pady=10)
date_entry = tkinter.Entry(cat_info_frame)
date_entry.grid(row = 3, column = 1, padx=10, pady=10)


#check in
check_in_label = tkinter.Label(cat_info_frame, text = 'Check in: ')
check_in_label.grid(row = 3, column = 2, padx=10, pady=10)
check_in_spinbox = tkinter.Spinbox(cat_info_frame, from_= 10.00, to = 17.00)
check_in_spinbox.grid(row = 3, column = 3, padx=10, pady=10)

#check out
check_out_label = tkinter.Label(cat_info_frame, text = 'Check out: ')
check_out_label.grid(row = 3, column = 4, padx=10, pady=10)
check_out_spinbox = tkinter.Spinbox(cat_info_frame, from_= 11.00, to = 18.00)
check_out_spinbox.grid(row = 3, column = 5, padx=10, pady=10)

#hour
duration_hour_label = tkinter.Label(cat_info_frame, text = 'Duration (Hour): ')
duration_hour_label.grid(row = 4, column = 0, padx=10, pady=10)
duration_hour_entry = tkinter.Entry(cat_info_frame)
duration_hour_entry.grid(row = 4, column = 1, padx=10, pady=10)


#cat's owner
#name
owner_name_label = tkinter.Label(cat_info_frame, text = 'Owner Name: ')
owner_name_label.grid(row = 2, column = 0, padx=10, pady=10)
owner_name_entry = tkinter.Entry(cat_info_frame)
owner_name_entry.grid(row = 2, column = 1, padx=10, pady=10)

#cats owner's cantact details
owner_phone_num_label = tkinter.Label(cat_info_frame, text = 'Phone Number : ')
owner_phone_num_label.grid(row = 2, column = 2, padx=10, pady=10)
owner_phone_num_entry = tkinter.Entry(cat_info_frame)
owner_phone_num_entry.grid(row = 2, column = 3, padx=10, pady=10)

#cat owner's address
owner_address_label = tkinter.Label(cat_info_frame, text = 'Address :')
owner_address_label.grid(row = 2, column = 4, padx=10, pady=10)
owner_address_entry = tkinter.Entry(cat_info_frame)
owner_address_entry.grid(row = 2, column = 5, padx=10, pady=10)

# Create a Button widget to trigger the calculation
calculate_button = tkinter.Button(cat_info_frame, text='Calculate', command=perform_calculation)
calculate_button.grid(row = 5, column = 0, padx=10, pady=10)


# Create a Label to display the calculation result
payment_label = tkinter.Label(cat_info_frame, text='Payment: ')
payment_label.grid(row = 5, column = 1, padx=10, pady=10)



button = ttk.Button(cat_info_frame, text='Save data', command=save_data)
button.grid(row=6, column=5, padx=10, pady=10)


root.mainloop()




