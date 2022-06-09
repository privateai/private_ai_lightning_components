from private_ai_synthetic_data_generator import PrivateAISyntheticData

def test_send_message():

    pai = PrivateAISyntheticData(
        key= 'INTERNAL_TESTING_UNLIMITED_REALLY',
        mode='standard',
        output_path='./',
        host='localhost',
        port='8080'
    )

    assert  isinstance(pai.run(input_text_or_path='Hi'), str)
    # assert pai.run(input_text_or_path='', action='', output_dir='') == None
