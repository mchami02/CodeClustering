print ('Loading Test...')
dtype_test = {'id':np.uint32,
              'Semana': np.uint8, 
              'Agencia_ID': np.uint16, 
              'Canal_ID': np.uint8,
              'Ruta_SAK': np.uint16, 
              'Cliente_ID': np.uint32, 
              'Producto_ID': np.uint16}

%time test = pd.read_csv('../input/test.csv', usecols=dtype_test.keys(), dtype=dtype_test)
test.head()