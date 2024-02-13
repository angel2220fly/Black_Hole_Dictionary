import os 

from time import time

import binascii

import math

import os.path



#@Author Jurijus Pacalovas



class compression:
    def compression_extract(self):
                          
                    
                    def process_info(INFO4, INFO_add, block=0, E=-1, A1=1):
                        long_file = len(INFO4)
                    
                       

                
  
                    def convert_and_decode_info(INFO):
                                                  
                             
                           
                                                    
                                                
                           n = int(INFO, 2)
                                                    
                           binary_data_length = len(INFO)
                              
                           hex_data_length = (binary_data_length // 8) * 2
                           binary_data_format = "%0" + str(hex_data_length) + "x"
                           binary_data = binascii.unhexlify(binary_data_format % n)
                           return binary_data                                    
                                    
                    self.name = "Created: Jurijus Pacalovas."
                    name = input("What is name of file? ")
               
                    
                    if os.path.exists(name):
                        print('Path is exists!')
                    else:
                        print('Path is not exists!')
                        raise SystemExit
                    


                    

                

                    
                 
                    


                    INFO3=""

                    INFO4=""
                    compress_1=""

                    stop_1_1=0
                    N_1=0
                    
    

                    name_1=name
                    

                    name_of_file=len(name_1)
                    name_find=name
                    
                    name_format_long=len(".Spring-200")

                    name_1=name+".Spring-200"
                    with open(name_1, "wb") as binary_file:
                        name_of_file=len(name_1)                

                    

                    

                    
                    
                    count_numbers=0

                    counts_1=2

                 

                    s=""


                    count_N=0

                

            

                 

                    INFO3=""

                    INFO_OR_DATA_TO_BINARY=""



                    

                    

                    binary_to_data=0
                    times_count=0
                    count_N3=0
                    stop_2=0
          
                



                   

        
    
                    count_N1=0
                    
                    reverse_1=0
                 
                    reverse_bin=0
                    count_N4=0
                    stop_2_1=0
                    count_N5=0
                   

        
                
                    
                    
                    

                    x=0

                    x1=0

                    x2=0
                    x5=0

                    x = time()



                    

                    with open("Dictionary.bin", "rb") as binary_file:

                       # Read the whole file at once

                        data1 = binary_file.read()
                        
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once

                        data = binary_file.read()
   
                        s=str(data)
                        C_E=0
                        file_bin=len(name_find)
                        if name_find[file_bin-name_format_long:]!=".Spring-200":
                                    C_E=1
                        elif name_find[file_bin-name_format_long:]==".Spring-200":
                                    C_E=2
                                    name_extract=name_find[:file_bin-name_format_long]
                                    
                                    
                       
                
                        long1=len(data)
                        long3=len(data)
                        stop_1=0

                        long5=len(data)
                        long5_before_1=len(data)
                        if long5_before_1>=2**32:
                            print("This is file is too big")
                            raise SystemExit
                        if long5_before_1==0:
                            raise SystemExit

                        times_numbers_reapits=0

                        binary_to_data_1=0

                        while times_numbers_reapits<10:
                            
                                counts_1=counts_1+1

                                count_numbers=count_numbers+1
                            
                                if count_numbers==1:
                                    # 256 range data to binary
                                    bits_long="0"+str(long1*8)+"b"



                                    b=int(binascii.hexlify(data),16)
                                    INFO=format(b,bits_long)
                                    
                                    bits_long="0"+str(long3*8)+"b"



                                    b1=int(binascii.hexlify(data1),16)
                                    INFO_D=format(b1,bits_long)                                    
                                    ####################
                                    
                                    if C_E==2:
                                        INFO1=""

                                        
                                        while INFO[:1]!="1":
                                                   if INFO[:1]=="0":
                                                       INFO=INFO[1:]

                                       

                                        INFO=INFO[1:]
                                        times_value_INFO=INFO[:32]
                                        times_value=int(times_value_INFO,2)
                                        INFO=INFO[32:]

                                        
                                                                            
                                    
                                    INFO_OR_DATA_TO_BINARY=INFO
                                    FF=INFO
                                    INFO11=INFO
                                    long3=len(INFO_OR_DATA_TO_BINARY)

                                long2=len(INFO_OR_DATA_TO_BINARY)
                                block=0
                                X=2
                                st=0
                                st1=0
                                                               
                                long_INFO = len(INFO)
                                long_file=len(INFO)
                                block2=0
                                INFO4=INFO
                                
                                #print(INFO4)
                               
                               
                                block=0
                                
                                
                                INFO1=""
                                INFO_add=""
                                INFO8=""
                                
                                E=-1
                                A1=1
                                INFO11=""
                         
                              
                                block=0
                                right=0
                                
                                if C_E==2:
                                    
                                    N_1+=1
                                    if N_1==times_value:
   
                                                 
                                                
                                                result_data = convert_and_decode_info(INFO)
                                                jl=result_data
                                                data = jl
                                                binary_to_data_1=binary_to_data_1+1
                                                reverse_bin=reverse_bin+1
                                                if reverse_bin==1:
            
                                                            times_numbers_reapits=10
            
                                                            if times_numbers_reapits==10:
                                                                
                                                                with open(name_extract, "wb") as binary_file:
                                                                    binary_file.write(jl)
            
                                                                x2 = time()
            
                                                                x3=x2-x
            
                                                                return print(x3)                                          
                                            
                                            
                                    
                                if C_E==1:
                                    
                                    INFO1=""
                                    
                                    #print(C_E)
                                
                                    INFO9=INFO 
                                    INFO4=INFO
                                    block=0
                                    add_INFO=""
                                    long_file=len(INFO4)

                                                                                                            
                                    INFO4=INFO
                                    block=0
                                    add_INFO=""
                                    long_file=len(INFO4)

                                        
                                    block=0
                                    INFO_add=""
                                    while block<long_file:
                                        program64bits = INFO4[block:block+26]
                                        
                                        
                                        
                                        x4 = INFO_D.find(program64bits,x5)
                                        #print(x4)
                                        x6=x4-x5
                                        b3=str(x6)
                                        b4=format(x6,'024b')
                                         
                                     
                                        
                                        
                                        if b3[:2]!="-1" and x6<=(2**24)-1:
                                            INFO1="1"+b4
                                            
                                     
                               
                                        else:
                                            
                                            INFO1="0"+program64bits
                                            #

                                            
                                        block+=26
                                        

                                        INFO_add+=INFO1
                                      
                                   
                                                                     

                                      
                                    
    
                                    count_N+=1
                                   # print(count_N)
                               
                                    INFO_OR_DATA_TO_BINARY1=INFO_add
                                    #print(INFO_add)
                                    INFO_OR_DATA_TO_BINARY=INFO_OR_DATA_TO_BINARY1
                                    INFO=INFO_OR_DATA_TO_BINARY

                                
                             
                                        
                                                                                                                                 
                                                                                                                                                                 
                                    
                                    s2=len(INFO)
                                    if s2>(long1*8):
                                        INFO=INFO_add
                                        stop_2+=1
                                        x5+=(2**20)-1
                                                                                             
                                                                               
                                    stop_1+=1                                                                                                                                                                                                         
                                    #print(len(INFO))                                  
 
                                    if count_N==(2**32)-1 or stop_2==30 or len(INFO)<=256:
                                            
                                            

                                            
                                            count_N=count_N4
                                            times_value=format(count_N,'032b')
                                           
                                            INFO=compress_1
                                            INFO=INFO
                                            if right==1:
                                                print("right compression and reverse")
                                            elif right==0:
                                                print("right compression and reverse")
                                            INFO="1"+INFO
                                            INFO=times_value+INFO
                               
                                            long1=len(INFO)
                                            xc=8-long1%8
    
                                            z=0
                                            if xc!=0 or xc!=8:
                                                    while z<xc:
                                                       INFO="0"+INFO
                                                       z=z+1
                                                       
                                            result_data = convert_and_decode_info(INFO)
                                             
                                            jl=result_data
                                            data = jl
                                            binary_to_data_1=binary_to_data_1+1
                                            reverse_bin=reverse_bin+1
                                            if reverse_bin==1:
        
                                                        times_numbers_reapits=10
        
                                                        if times_numbers_reapits==10:
                                                            
                                                            with open(name_1, "wb") as binary_file:
                                                                binary_file.write(jl)
        
                                                            x2 = time()
        
                                                            x3=x2-x
        
                                                            return print(x3)
                                                    
                                                          
d=compression()



xw=d.compression_extract()

print(xw)
