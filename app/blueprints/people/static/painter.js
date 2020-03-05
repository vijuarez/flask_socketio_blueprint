const peer_self = new Peer();


draw = () => {
    localStorage.debug = '*';

    const socket = io('/people', {
        transports: ['websocket']
      });

    peer_self.on('open', (id) => {
        console.log('we connected');
        socket.emit('new_friend', id);
    });

    socket.on('new_friend_reg', (x) => {
        console.log('server spoke back');
    })
};