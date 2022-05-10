import paramiko
from tkinter import *
import pandas as pd
import uuid
from pprint import pprint


def is_valid_uuid(value):
    try:
        uuid.UUID(value)

        return True
    except ValueError:
        return False


def lookup_UUID(UUID):
    '''
    Use Paramiko to retrieve the entire 'show version' output.
    '''


    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('HOST',username='NAME',password='PASSWORD')
    sftp_client = client.open_sftp()
    with sftp_client.open('/net/europa2/work/afenton/Documents/SPH_simulations/simulation_database.txt') as file:
        df = pd.read_csv(file,sep=' ',header=None)
        df.columns=['UUID', 'star_mass', 'disc_mass', 'disc_radius', 'r_inner', 'p_index', 'q_index', 'tmax',
                    'artvisc', 'rhocrit1', 'rhocrit2', 'rhocrit3', 'gamma1', 'gamma2', 'gamma3', 'resolution','path']


    selected = df.loc[df['UUID'] == UUID]

    UUID = selected['UUID'].values
    star_mass = selected['star_mass'].values
    disc_mass = selected['disc_mass'].values
    disc_radius = selected['disc_radius'].values
    r_inner = selected['r_inner'].values
    p_index = selected['p_index'].values
    q_index = selected['q_index'].values
    tmax = selected['tmax'].values
    artvisc = selected['artvisc'].values
    rhocrit1 = selected['rhocrit1'].values
    rhocrit2 = selected['rhocrit2'].values
    rhocrit3 = selected['rhocrit3'].values
    gamma1 = selected['gamma1'].values
    gamma2 = selected['gamma2'].values
    gamma3 = selected['gamma3'].values
    resolution = selected['resolution'].values
    path = selected['path'].values
    returned_string = ("""UUID = %s \nStar Mass = %s Solar Masses \nDisc Mass = %s Solar Masses \nDisc Radius = %s AU \nR Inner = %s AU \np Index = %s \nq Index = %s
tmax = %s Code Units \ntmax = %s Years \nArtifical Viscosity = %s \nrhocrit1 = %s g/cm^3 \nrhocrit2 = %s g/cm^3  \nrhocrit3 = %s g/cm^3  \ngamma1 = %s \ngamma2 = %s \ngamma3= %s \nResolution = %s particles \nFull Path= %s \n"""\
                        %(UUID[0],star_mass[0],disc_mass[0],disc_radius[0],r_inner[0],p_index[0],q_index[0],tmax[0],(tmax[0] * 5.023E6)/3.15E7,artvisc[0],rhocrit1[0],rhocrit2[0],rhocrit3[0],
                          gamma1[0],gamma2[0],gamma3[0],resolution[0],path[0]))
    return returned_string


def lookup_other(quantity,value):
    '''
    Use Paramiko to retrieve the entire 'show version' output.
    '''


    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('HOST',username='NAME',password='PASSWORD')
    sftp_client = client.open_sftp()
    with sftp_client.open('/net/europa2/work/afenton/Documents/SPH_simulations/simulation_database.txt') as file:
        df = pd.read_csv(file,sep=' ',header=None)
        df.columns=['UUID', 'star_mass', 'disc_mass', 'disc_radius', 'r_inner', 'p_index', 'q_index', 'tmax',
                    'artvisc', 'rhocrit1', 'rhocrit2', 'rhocrit3', 'gamma1', 'gamma2', 'gamma3', 'resolution','path']


    selected = df.loc[df[quantity] == value]


    return selected['UUID'].values







def draw_GUI():

    def redirector(inputStr):
        textbox.insert(INSERT, inputStr)


    sys.stdout.write = redirector
    ws = Tk()
    ws.title('Simulation Query')
    ws.geometry('800x700')
    ws.config(bg='black')



    query = Entry(ws,width=50,font=('Arial', 24))

    def sort_query(query):
        if is_valid_uuid(query.get()) == True:
            return lookup_UUID(query.get())
        elif is_valid_uuid(query.get()) == False :
            quantity = query.get().split(" ")[0]
            value = query.get().split(" ")[1]
            print("Simulations matching request:")
            return lookup_other(str(quantity),float(value))

            # print(lookup_other(str(quantity),float(value)))


    #
    query_lbl = Label(
    ws,
    text='Query',
    bg='black',
    fg='white',
    font=('Arial', 15)
    )
    #
    query_lbl.pack()
    query.pack()
    #
    #
    #
    btn = Button(
    ws,
    text='Request run paramaters',
    relief=SOLID,
    bg='black',
    height=5,
    font=('Arial', 24),
    command=lambda: print(sort_query(query))
    )
    #
    #
    #
    textbox=Text(ws,font=('Arial', 18),height=21,width=50,fg='white')
    btn.pack(pady=15)
    #
    textbox.pack()
    #
    #
    #
    #
    #
    #


    ws.mainloop()
if __name__ == "__main__":
    draw_GUI()
