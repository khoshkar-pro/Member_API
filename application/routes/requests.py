from application import app

@app.route('/member', methods=['GET'])
def get_members():
    return 'This returns all the members.'
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    return 'This returns one member by ID'
@app.route('/member', methods=['POST'])
def add_member():
    return 'This adds a new member.'
@app.route('/member/<int:member_id>', methods=['PUT', 'PATCH'])
def edit_member(member_id):
    return 'This updates a member by ID.'
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    return 'This removes a member by ID.'