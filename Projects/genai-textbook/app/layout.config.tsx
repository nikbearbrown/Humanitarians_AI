import Image from 'next/image';
import Logo from '@/public/logo.png';
import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';

export const baseOptions: BaseLayoutProps = {
  nav: {
    title: (
      <div className="flex items-center space-x-2">
        {/* Logo image */}
        <Image
          src={Logo}
          alt="Gen AI Textbook Logo"
          width={32}   // Adjust size as needed
          height={32}  // Adjust size as needed
        />

        {/* Title text */}
        <span className="text-sm font-medium">
          Gen AI Textbook
        </span>
      </div>
    ),
  },
};
