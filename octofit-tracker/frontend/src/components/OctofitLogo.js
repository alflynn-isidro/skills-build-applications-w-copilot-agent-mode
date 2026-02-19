import React from 'react';
import logo from '../docs/octofitapp-small.png';

const OctofitLogo = ({ height = 40 }) => (
  <img src={logo} alt="Octofit Logo" height={height} style={{ marginRight: 12, verticalAlign: 'middle' }} />
);

export default OctofitLogo;
