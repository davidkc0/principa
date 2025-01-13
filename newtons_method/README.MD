float Q_rsqrt( float number )
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;						// evil floating point bit level hacking
	i  = 0x5f3759df - ( i >> 1 );               // what the fuck?
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
//	y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

	return y;
}

https://en.wikipedia.org/wiki/Fast_inverse_square_root


\chapter{Animation, Computer Vision, and Graphics}
\section{Creating Timelapses}
\section{Working with FFMPEG and GIFs}
\section{Rendering 3D Line Illustrations}
\section{Photogrammetry and 3D Vision}
\section{Nonphotorealistic Rendering Techniques}

Numerical approximation.
Newtons method, and Q_rsqrt
