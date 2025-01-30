from contacts.forms import NameForm

def test_name_form_success():
    data= {"your_name": "John"}
    
    form = NameForm(data)
    
    is_valid = form.is_valid()
    
    assert is_valid is True

def test_name_form_fail():
    data= {}
    
    form = NameForm(data)
    
    is_valid = form.is_valid()
    is_bound = form.is_bound
    
    assert is_valid is False
    assert is_bound is True

def test_name_form_max_length():
    data= {"your_name": "John"*50}
    
    form = NameForm(data)
    
    is_valid = form.is_valid()
    
    assert is_valid is False
    assert form.errors == {
        "your_name": ["Certifique-se de que o valor tenha no máximo 100 caracteres (ele possui 200)."]
    }
